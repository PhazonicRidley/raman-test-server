// @ts-check

console.log("We're alive")

function connect() {
    const socket = new WebSocket("ws://localhost:8765");
    // Connection opened
    socket.addEventListener('open', (event) => {
        socket.send('Hello Server!');
    });

    // Listen for messages
    socket.addEventListener('message', (event) => {
        console.log('Message from server ', event.data);
    });

    return socket
}


function button_pushed() {
    const socket = connect()
    console.log("Button logged.");
    socket.send("Button pushed.")

}
