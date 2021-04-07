const app = new Vue({
    el: '#app',
    data: {
     title: 'Nestjs Websockets UI',
     imageBytes: '',
     socket: null,
     decoder: new TextDecoder(),
     canvas: null,
     canvasElem: null
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
                this.canvas.rect(...box.rect);
                this.canvas.strokeStyle = "red"
                this.canvas.stroke();
            });
        }
    }
   },
    mounted() {
        this.socket = io('http://10.0.0.7')
        this.socket.on('image', (message) => {
            this.receivedMessage(message)
        })
        this.canvasElem = document.getElementById("myCanvas")
        this.canvas = this.canvasElem.getContext("2d")
    }
   })