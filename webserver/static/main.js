const app = new Vue({
    el: '#app',
    data: {
     title: 'Nestjs Websockets UI',
     imageBytes: '',
     socket: null,
     decoder: new TextDecoder()
    },
    methods: {
     receivedMessage(message) {
        this.imageBytes = this.decoder.decode(new Uint8Array(message.image));
    }
   },
    created() {
     this.socket = io('http://10.0.0.7')
     this.socket.on('image', (message) => {
      this.receivedMessage(message)
     })
    }
   })