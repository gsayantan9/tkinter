// pub fn func(arg: &mut Vec<i32>) -> Vec<i32> {
//     arg.push(1);
//     return arg.to_vec();
// }

pub fn gcd(mut a: u32, mut b: u32)->u32 {
    assert!(a>0 && b>0);
    if b > a {
        // let mut remainders_list = vec![];
        // let mut remainders_list = Vec::new();
        let mut r = b % a;
        // if r == 1 {
        //     println!("gcd is {}",r);
        // }
        while r != 0 {
            // remainders_list.push(r);
            // println!("{},{},{}", a, b, r);
            b = a;
            a = r;
            r = b % a;
        }
        // println!("the remainder list is {:?}",remainders_list);
        // println!("{},{},{}", a, b, r);
        // println!("gcd is {}",a);
        a
    }
    else {
        gcd(b, a)
    }
}

pub fn gcs(mut n: u64, mut m: u64) -> u64 {
    assert!(n != 0 && m != 0);
    while m != 0 {
    if m < n {
    let t = m;
    m = n;
    n = t;
    }
    m = m % n;
    }
    println!("gcs is {}",n);
    n
   }

   

