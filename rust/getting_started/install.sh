### https://www.rust-lang.org/learn/get-started


# Download Rustup and install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Update
rustup update

## Cargo: Rust build tool and package manager
# build your project with 
cargo build
#run your project with
cargo run
#test your project with
cargo test
#build documentation for your project with
cargo doc
#publish a library to crates.io with 
cargo publish
# test
cargo --version

## Start a new project
cargo new hello-rust
# Cargo.toml: manifest file
# src/main.rs: application code


## Add dependencies
# https://crates.io/
cargo add ferris-says@0.2
# Install dependencies
cargo build


