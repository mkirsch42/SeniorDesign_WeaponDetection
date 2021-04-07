const app = new Vue({
    el: '#app',
    data: {
     imageBytes: '',
     socket: null,
     decoder: new TextDecoder(),
     canvas: null,
     canvasElem: null,
     notifications: []
    },
    methods: {
     receivedMessage(message) {
        this.imageBytes = this.decoder.decode(new Uint8Array(message.image));
        var img = new Image();
        img.src = "data:image/jpeg;base64," + this.imageBytes;
        img.onload = ()=>{
            this.canvas.clearRect(0, 0, this.canvasElem.width, this.canvasElem.height)
            this.canvas.drawImage(img, 0, 0)
            message.boxes.forEach(box => {
                this.canvas.beginPath();
                this.canvas.strokeStyle = box.label.color
                this.canvas.lineWidth = 4
                this.canvas.rect(...box.rect);
                this.canvas.stroke();

                this.canvas.font = "24px Arial"
                this.canvas.textBaseline = "top"
                this.canvas.fillStyle = box.label.color
                this.canvas.fillRect(box.rect[0], box.rect[1], this.canvas.measureText(box.label.name).width + 2, 26)
                this.canvas.fillStyle = box.label.fg
                this.canvas.fillText(box.label.name, box.rect[0] + 1, box.rect[1] + 1)

                notif = this.notifications.find(notif => 
                    notif.label == box.label.name
                    && notif.timer > 0)
                if (notif) {
                    notif.timer = 15
                } else {
                    this.notifications.push({
                        timer: 15,
                        label: box.label.name,
                        timestamp: new Date().toLocaleTimeString(),
                        thumbnail: this.canvasElem.toDataURL()
                    })
                }

            });
        }
    },
    downTickNotifications() {
        this.notifications.forEach(notif => {
            notif.timer -= 1;
        });
        // this.notifications = this.notifications.filter(notif => notif.timer > 0);
    }
   },
    mounted() {
        this.socket = io()
        this.socket.on('image', (message) => {
            this.receivedMessage(message)
        })
        this.canvasElem = document.getElementById("myCanvas")
        this.canvas = this.canvasElem.getContext("2d")
        window.setInterval(this.downTickNotifications, 1000);
    }
   })