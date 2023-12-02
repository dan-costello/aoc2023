mod day1;
mod day2;

fn main() {
    let args = std::env::args().collect::<Vec<String>>();

    match args.len() {
        2 => match args[1].as_str() {
            "day1" => day1::run(),
            "day2" => day2::run(),
            _ => eprintln!("Invalid argument!"),
        },
        _ => println!("Hello, world!"),
    }
}
