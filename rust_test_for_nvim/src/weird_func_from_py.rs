// pub fn func(arg: &mut Vec<i32>) -> Vec<i32> {
//     arg.push(1);
//     return arg.to_vec();
// }

pub fn gcd(mut a: i32, mut b: i32) {
    // assert!(b > a);
    if b > a {
        // let mut remainders_list = vec![];
        let mut remainders_list = Vec::new();
        let mut r = b % a;
        if r == 1 {
            println!("gcd is {}",r);
        }
        while r > 0 {
            r = b % a;
            remainders_list.push(r);
            println!("{},{},{}", a, b, r);
            b = a;
            a = r;
        }
        println!("the remiander list is {:?}",remainders_list);
    }
    else {
        gcd(b, a);
    }

}
