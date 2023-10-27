mod weird_func_from_py;
use weird_func_from_py::{gcd,gcs};
fn main() {
    println!("hello world!");
    println!("{}",gcd(12, 18));
    println!("{}",gcd(2 * 3 * 5 * 11 * 17,3 * 7 * 11 * 13 * 19));
    gcs(7, 3);
}

#[test]
fn test_gcd() {
    println!("{:?}",assert_eq!(gcd(14, 15), 1));
    println!("{:?}",assert_eq!(gcd(2 * 3 * 5 * 11 * 17,
        3 * 7 * 11 * 13 * 19), 3 * 11));
   }

// #[test]
// fn test_gcs() {
//     println!("{:?}",assert_eq!(gcd(14, 15), 1));
//     println!("{:?}",assert_eq!(gcd(2 * 3 * 5 * 11 * 17,
//         3 * 7 * 11 * 13 * 19), 3 * 11));
//     }