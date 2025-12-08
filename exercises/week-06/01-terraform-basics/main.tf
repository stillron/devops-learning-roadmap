resource "local_file" "hello" {
    content = "Goodbye from Terraform!"
    filename = "${path.module}/hello.txt"
}