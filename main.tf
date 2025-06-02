provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "bad_bucket" {
  bucket = "insecure-bucket-public-read"
  acl    = "public-read"

  tags = {
    Name        = "bad_bucket"
    Environment = "test"
  }
}
