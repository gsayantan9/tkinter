mod weird_func_from_py;
use weird_func_from_py::gcd;
fn main() {
    println!("hello world!");

    for i in 0..10 {
        println!("{}", i);
    }
    gcd(18, 12);
}