# Solution
# [+] -=-=-= HCMUS-CTF 2021 =-=-=-
# [-] PIS-concainit team


# PIS-concainit.zirami
  
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




# PIS-concainit.hlong

`https://github.com/hlong12042/WRITE-UP-HCMUS-CTF-2021`

# PIS-concainit_MR

## Faded.

Faded description nhắc đến thông tin về việc gen file executable từ python code.
Mình sẽ thử tìm và decompile từ file elf này thành python code.
Sử dụng utility pyi-archive_viewer của module python PyInstaller, giải mã ra được file authentication
Thử cat strings file này thì mình xuất ra được flag
`>>> FLAG:  HCMUS-CTF{Python_is_fun_somehow}`

## WeirdProtocol

Kiểm tra thông tin file WeirdProtocol với Detect It Easy thấy có file BINARY lạ trong phần resorces PE,
 Dump file này ra để kiểm tra thì đây là file exe 32bit.
Khi chạy test thử thì file này LISTEN local 127.0.0.1:4919 nên đây có thể là file server để WeirdProtocol.exe kết nối đến.
Mở và kiểm tra WeirdProtocol.exe với IDA, chương trình gửi đến server độ dài dữ liệu nhập và tiếp theo là dữ liệu nhập.
Chuỗi "[+] Fail, reconnecting ...\n" sẽ luôn được in ra nên đây sẽ không phải là lỗi khi chạy chương trình.

* `Link image`

```sh
https://www.notion.so/HCMUS-CTF-2021-b967b6b0a8f54f3ca59a54f38470e5c5
```

 Tiếp tục kiểm tra file server với IDA, ở hàm main mình thấy server sẽ kiểm tra và thực hiện xor dữ liệu nhận từ client với các ký tự tương ứng ở được định nghĩa ở biến v6 (30 ký tự).
 
Mình đem xor format flag của CTF với các ký tự đầu của dãy v6 thì thấy được giá trị nhận từ client sẽ là chuỗi ký tự "hellohello..." (30 ký tự)
Khi chạy thử với input client là chỗi hello, server chỉ trả về giá trị là "Nice try buddy", tiếp tục kiểm tra và mình patch program server để bypass đoạn kiểm tra Buf1, Buf2. Path program jnz -> jz
 
Thử chạy lại và mình lấy được flag của chương trình gửi từ server.

`>>> FLAG: HCMUS-CTF{not_so_weird_hehexd}`

## Androidrev

link bài viết.
`https://www.notion.so/HCMUS-CTF-2021-b967b6b0a8f54f3ca59a54f38470e5c5`

# PIS-concainit.V

`>>> Link: https://www.notion.so/HCMUS-CTF-41fe38bfe5914d3c88f507947451386b`
