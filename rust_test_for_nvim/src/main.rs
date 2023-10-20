mod weird_func_from_py;
use weird_func_from_py::func;
fn main() {
    println!("hello world!");

    for i in 0..10 {
        println!("{}", i);
    }
    println!("{:?}",func(vec![1]));
    func();
}
