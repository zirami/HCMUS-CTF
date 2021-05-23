# HCMUS-CTF
 
# SOLUTION 


## MyBirthDay
### Sourcecode
```sh
  char buf[24]; // [esp+0h] [ebp-24h] BYREF
  int v5; // [esp+18h] [ebp-Ch]
  int *v6; // [esp+1Ch] [ebp-8h]

  v6 = &argc;
  v5 = -17829890;
  setup();
  puts("Tell me your birthday?");
  read(0, buf, 0x1Eu);
  if ( v5 == 0xCABBFEFF )
    run_cmd("/bin/bash");
  else
    run_cmd("/bin/date");
  return 0;
```
Bài này chỉ cần làm sao cho biến V5 thỏa điều kiện là được 1 cái shell.

`>>> FLAG:  HCMUS-CTF{Just_A_Warm_Up_Pwn}`

## Bank1
```sh
**nc 61.28.237.24 30202**

[+] Please enter your name: PIS-concainit PIS-zirami PIS-MR PIS-V PIS-Hlong 
[+] Thanks for the registration, your balance is 0.
[+] Good bye!

```
Bank1 chỉ cần làm thay đổi biến your balance khác 0 nè!!!

`>>> FLAG: HCMUS-CTF{that_was_easy_xd}`

## Bank2

```sh
char name[64]; // [esp+Ch] [ebp-4Ch] BYREF
  int balance; // [esp+4Ch] [ebp-Ch]

  balance = 0;
  printf("[+] Please enter your name: ");
  gets(name);
  printf("[+] Thanks for the registration, your balance is %d.\n", balance);
  if ( balance == 0x66A44 )
    getFlag();
```

Bài này cấu trúc giống như bài Mybirthday vậy, chỉ cần thay đổi biến `balance == 0x66a44`.

`>>> FLAG: HCMUS-CTF{little_endian_is_fun}`


## Bank3

```sh
void getFlag()
{
  system("cat flag.txt");
}
```
Bài này chuyển ControlFlow về func getFlag() sẽ in ra được flag.

`>>> FLAG: HCMUS-CTF{overwrite_all_the_things}`

## Bank4

```sh
void getFlag()
{
  if ( o1 && o2 )
    system("cat flag.txt");
  else
    system("echo \"hcmasd-cft{nah_nah_nah_not_today}\"");
}
```

Bài này cũng có hàm getFlag() như có điều kiện, mình thấy có 2 cách là: `chuyển ControlFlow về system("cat flag.txt)` hoặc làm cho `o1 và o2 true`. 

`>>> FLAG: HCMUS-CTF{trungdeptrai}`

## Bank5

* Không có hàm để nhảy đến.
* Bài này build `STATIC` nên không có thư viện.
* No PIE
* `Dùng ROP chain để get shell.`

`>>> FLAG: HCMUS-CTF{rop_and_shellcode}`

## Bank6

```sh
char name[1024]; // [esp+Ch] [ebp-40Ch] BYREF
  int balance; // [esp+40Ch] [ebp-Ch]

  balance = 0;
  printf("[+] Here is a gift: %p\n", name);
  printf("[+] Please enter your name: ");
  __isoc99_scanf("%1036s", name);
  printf("[+] Thanks for the registration, your balance is %d.\n", balance);
```
* Bank6 cho sẵn 1 món quà, địa chỉ stack: là nơi mình ghi shellcode
* Tính offset là quá sức của mình, nên mình tạo 1 vùng đủ lớn bằng ` món quà địa chỉ `. :3
* Return the shellcode. `( note: func scanf chặn 0x0...)`

`>>> FLAG: HCMUS-CTF{0ff_by_on3}`


## SecretWeapon


```sh
`func townsquare`

char v1[20]; // [esp+0h] [ebp-18h] BYREF

  puts("You wanna open the arsenal. Tell me the passphrase!");
  printf("Your current location is townsquare with the address %p \n", townsquare);
  return __isoc99_scanf("%s", v1);
```
* Chương trình có 4 func: setup, run_cmd, arsenal, townsquare.
* hàm `run_cmd(command)` có `system(command)`.
* hàm arsenal có: `run_cnd("/bin/bash")`

--> Chuyển ControlFlow về arsenal.

`>>> FLAG: HCMUS-CTF{you_know_how_to_compute_location}`

## Dogge

` ssh ctf@61.28.237.24 -p30400 password: hcmus-ctf `

* Server có bin và flag.txt
* `. flag.txt`

`>>> HCMUS-CTF{You_know_some_command_line_stuff}`

## TheChosenOne

* Mã hóa khối AES - mode ECB 
* Dùng ` kí tự D` lấp đầy số bit còn lại, thêm sau input nhập vào.
* Các khối mã hóa riêng biệt.
* Cùng 1 plaintext --> 1 ciphertext
* Dùng bruteforce từng kí tự flag, kiểm tra khối đúng với khối brute, nếu giống nhau thì `kí tự brute` thuộc flag.

`>>> FLAG: HCMUS-CTF{You_Can_4ttack_A3S!?!}`

## FADE

* Dùng tool `pyi-archive-viewer` như sau:
* `pyi-archive-viewer authentication (tên file) `
* `X authentication (tên file)`
* `to file name? output.txt (Nhập tên file output)`
* `Q (quit)`
* `cat file output`

`>>> FLAG: HCMUS-CTF{Python_is_fun_somehow}`

