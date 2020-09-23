import hashlib
import time
import os
os.system("clear")
banner = """  \033[0;31m                                                                                                           
           0 0---------------------------------------------------------------------------------------------------------------------0 0
           0 0---------------------------------------------------------------------------------------------------------------------0 0
           | |     $**$       $*$*$*$*$*$        $*$$*$$*$$*$   $*$*$*$*$*$      $*$          $*$       $**$       $*$             | |
           | |   $*$  $*$     $*$      )*)       $*$      $*$   $*$      )*)     $*$          $*$     $*$  $*$     $*$             | |
           | | $*$      $*$    $*$     )*)       $*$      $*$     $*$    )*)      $*$        $*$    $*$      $*$   $*$             | |
           | | $*$      $*$     $*$              $*$      $*$      $*$              $*$    $*$      $*$      $*$   $*$             | |
           | | $*$&&&&&&$*$       $*$$*$)*)      $*$      $*$        $*$$*$)*)        $*$$*$        $*$&&&&&&$*$   $*$             | |
           | | $*$      $*$              $*$     $*$      $*$               $*$         $$          $*$      $*$   $*$             | |         
           | | $*$      $*$   $*$         $*$    $*$      $*$   $*$          $*$        $$          $*$      $*$   $*$         )*) | |
           | | $*$      $*$   (*(*$*$*$*$*$)*)   $*$$*$$*$$*$   (*(*$*$*$*$*$)*)     $*$$*$$*$      $*$      $*$   $*$$*$$*$$*$$*$ | |
           0 0---------------------------------------------------------------------------------------------------------------------0 0
           0 0---------------------------------------------------------------------------------------------------------------------0 0
                                                         HASH METODUYLA SIFRELEME ARACI
                                                                                                                                                                                                                       
                                             00      [++++++++++++++++++++++++++++++++++++]     00                                               
                                             ||   >~  TOPLUM ***:::***>> AYNI fARKLILIKLAR ~<   ||                                    
                                             ||      [++++++++++++++++++++++++++++++++++++]     ||                                    
                                             ||               [101]  (((_)))  [111]             ||                                 
                                             ||               [011]     !     [011]             ||                                    
                                             ||                [100]   !@!   [100]              ||                                    
                                             ||                  [001]     [101]                ||                                    
                                             ||                     [1010101]                   ||                                    
                                             ||                                                 ||                                    
                                             \/                                                 \/ \033[0m 
                                               \033[5;37;1m                  *)--ASOSYAL-- (*\033[0;0m
                                                   

                                                                                                                                     
"""                                                                                                                                   
print(banner)           


class hashlama():

    def hashlama_secenegi(self):
       print("\033[0;33;40mVeri sifreleme salonuna hos geldiniz.\nSifreleme sinifindan birisini secerek , prosedurunuza baslaya bilirsiniz. ")

       print("\033[0;33;40m[1] md5 sifreleme\n[2] sha256 sifreleme\n[3] sha1 sifreleme\n[4] sha512 sifreleme\n[5] sha224 sifreleme\n[6] sha384 sifreleme ")
       secim = input("Secim:::===>>>")
       if (secim == "1"):
         self.md5_sifrelenmesi()
       elif (secim == "2"):
           self.hsa_sifrelenmesi()
       elif (secim == "3"):
           self.hsa1_sifrelenmesi()
       elif (secim == "4"):
           self.hsa512_sifrelenmesi()
       elif (secim == "5"):
           self.hsa224_sifrelenmesi()
       elif (secim == "6"):
           self.hsa384_sifrelenmesi()
       else:
           print("\033[1;31;40mSeciminiz uzere bir prosedur yok[-]\nyanlis mudahilede bulundunuz[-]\033[0m")
       yeni_secim = input(
           "yeni bir veri sifrelemek istermisiniz? , eger istersenez E diye aksi takdirde H diye bir secim girin:::===>>>")

       if (yeni_secim == "E"):
           print(self.hashlama_secenegi())

       elif (yeni_secim == "H"):
           print("ISLEMINIZ SONA ERMISDR")
       else:
           print("\033[1;31;40m YANLIS MUDAHILEDE BULUNDUNUZ, BILGILERE UYGUN HARAKET EDIN!!!\033[0m")



    def md5_sifrelenmesi(self):

        veri_aktarimi = input("md5'le haslamak icin degerinizi dahil ediniz:::===>>>")
        print("biraz bekleyin degeriniz hash'lama makinesine aktariliyor")
        time.sleep(3)
        print("hash'lama makinesi degerinizi sifrelemisdir[+]\nSisfreniz 5 saniye sonra ekrana basdirilicakdir")
        time.sleep(5)
        deger_sifrelenmesi = hashlib.md5(veri_aktarimi.encode())
        print("::::===>>>",deger_sifrelenmesi.hexdigest(),"<<<===::::")

    def hsa_sifrelenmesi(self):
        veri_aktarimi = input("sha256'la haslamak icin degerinizi dahil ediniz:::--->>>")
        print("biraz bekleyin degerinizi hash'lama makinesine aktariliyor")
        time.sleep(3)
        print("hash'lama makinesi degeriniz sifrelemisdir[+]\nSisfreniz 5 saniye sonra ekrana basdirilicakdir")
        time.sleep(5)
        deger_sifrelenmesi = hashlib.sha256(veri_aktarimi.encode())
        print("::::===>>>", deger_sifrelenmesi.hexdigest(), "<<<===::::")

    def hsa1_sifrelenmesi(self):
        veri_aktarimi = input("sha1'la haslamak icin degerinizi dahil ediniz:::--->>>")
        print("biraz bekleyin degeriniz hash'lama makinesine aktariliyor")
        time.sleep(3)
        print("hash'lama makinesi degeriniz sifrelemisdir[+]\nSisfreniz 5 saniye sonra ekrana basdirilicakdir")
        time.sleep(5)
        deger_sifrelenmesi = hashlib.sha1(veri_aktarimi.encode())
        print("::::===>>>", deger_sifrelenmesi.hexdigest(), "<<<===::::")

    def hsa512_sifrelenmesi(self):
        veri_aktarimi = input("sha512'la haslamak icin degerinizi dahil ediniz:::--->>>")
        print("biraz bekleyin degeriniz hash'lama makinesine aktariliyor")
        time.sleep(3)
        print("hash'lama makinesi degeriniz sifrelemisdir[+]\nSisfreniz 5 saniye sonra ekrana basdirilicakdir")
        time.sleep(5)
        deger_sifrelenmesi = hashlib.sha512(veri_aktarimi.encode())
        print("                    \n::::===>>>", deger_sifrelenmesi.hexdigest(), "<<<===::::")

    def hsa224_sifrelenmesi(self):
        veri_aktarimi = input("sha224'la haslamak icin degerinizi dahil ediniz:::--->>>")
        print("biraz bekleyin degeriniz hash'lama makinesine aktariliyor")
        time.sleep(3)
        print("hash'lama makinesi degeriniz sifrelemisdir[+]\nSisfreniz 5 saniye sonra ekrana basdirilicakdir")
        time.sleep(5)
        deger_sifrelenmesi = hashlib.sha224(veri_aktarimi.encode())
        print("::::===>>>", deger_sifrelenmesi.hexdigest(), "<<<===::::")

    def hsa384_sifrelenmesi(self):
        veri_aktarimi = input("sha384'la haslamak icin degerinizi dahil ediniz:::--->>>")
        print("biraz bekleyin degeriniz hash'lama makinesine aktariliyor")
        time.sleep(3)
        print("hash'lama makinesi degeriniz sifrelemisdir[+]\nSisfreniz 5 saniye sonra ekrana basdirilicakdir")
        time.sleep(5)
        deger_sifrelenmesi = hashlib.sha384(veri_aktarimi.encode())
        print("::::===>>>", deger_sifrelenmesi.hexdigest(), "<<<===::::")
calistir = hashlama()
calistir.hashlama_secenegi()

