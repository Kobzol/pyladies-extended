struct Connection;

struct ConnectedClient {
    conn: Connection
}

impl ConnectedClient {
    fn send_message(&self, message: &str) {

    }

    fn close(self) {}
}

fn connect(address: &str) -> Result<ConnectedClient, String> {
    panic!()
}

fn client() {
    let client = connect("address").unwrap();
    client.send_message("hello");
    if 1 < 2 {
        client.close();
    }
    client.send_message("hello 2");
}
