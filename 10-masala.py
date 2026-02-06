# # 1-masala
# class Transport:
#     def __init__(self, model: str, yil: int) -> None:
#         self.model = model
#         self.yil = yil
#
#     def malumot(self) -> str:
#         return f"Model: {self.model}, Yil: {self.yil}"
#
#
# class Avtomobil(Transport):
#     def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, Yonilg'i: {self.yonilgi_turi}"
#
#
# class Avtobus(Transport):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"
#
#
# a = Avtomobil("Cobalt", 2022, "benzin")
# print(a.malumot())
#
# b = Avtobus("Isuzu", 2018, 40)
# print(b.malumot())


# # 2-masala
# class kitob:
#     def __init__(self, nom, muallif, yil):
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = 0
#
#     def taqdimot(self)  -> str:
#         return "\"{nom}\" - {muallif} ({yil})"
#
# class ElektronKitob(kitob):
#     def __init__(self, nom, muallif, yil: int, fayl_hajmi_mb: str) -> None:
#         super().__init__(nom, muallif, yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def taqdimot(self) -> str:
#         return "[Elektron, {fayl_hajmi_mb}MB]"
#
#
# class AudioKitob(kitob):
#     def __init__(self, nom, muallif, yil: int, davomiylik_soat: int) -> None:
#         super().__init__(nom,muallif, yil)
#         self.davomiylik_soat =davomiylik_soat
#
#     def taqdimot(self) -> str:
#                 davomiylik_soat = super().taqdimot()
#                 return f"[Audio, {davomiylik_soat} soat]"
#
# e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
# a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
#
# print(e.taqdimot())
# print(a.taqdimot())

# # 3-masala
# class xodim:
#     def __init__(self, ism, asosiy_maosh):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
#
#     def oylik(self) -> str:
#         return "asosiy_maosh"
#
#     def malumot(self) -> str:
#         return "Ism: {ism}, Oylik: {oylik()}"
#
# class Oqsoch(xodim):
#     def __init__(self, ism, asosiy_maosh, bonus_foiz):
#         super().__init__(ism, asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
#
#     def oylik(self) -> str:
#         return "oylikka {bonus_foiz} bonus qo'shilsin"
#
# class SoatbayXodim(xodim):
#     def __init__(self, ism, asosiy_maosh, bonus_foiz, soat, soatlik_stavka):
#         super().__init__(soat, soatlik_stavka)
#         self.soatlik_stavka = soatlik_stavka
#
#     def malumot(self) -> str:
#         soatlik_stavka = super().asosiy_maosh()
#         return "{soat}, O'rinlar: {self.soatlik_stavka}"
#
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)
#
# print(o.malumot())
# print(s.malumot())

# # 5-masala
# class shaxs:
#     def __init__(self, ism):
#         self.ism = ism
#
# class talaba(shaxs):
#     def __init__(self, ism, id_raqam):
#        super().__init__(ism)
#        self.id_raqam = id_raqam
#
# class ImtihonNatijasi(talaba):
#     def __init__(self, ism, id_raqam, baholar):
#         super().__init__(ism, id_raqam)
#         self.baholar = baholar
#
#     def ortalama (self):
#         if not self.baholar:
#             return 0.0
#         return sum(self.baholar) / len(self.baholar)
#
#     def status(self):
#         o = self.ortalama()
#         if o >= 86:
#             return "A'lo"
#         elif 71 <= o <= 85:
#             return "Yaxshi"
#         elif 56 <= o <= 70:
#             return "Qoniqarli"
#         return "Qoniqarsiz"
#
#
# natija = ImtihonNatijasi("Doniyor", "U001", [80, 70, 60, 50])
#
# print(natija.ism)
# print(natija.id_raqam)
# print(natija.ortalama())
# print(natija.status())

# # 6-masala
# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.egasi = egasi
#         self.balans = balans
#
#     def kirim(self, summa):
#         self.balans += summa
#
#     def chiqim(self, summa):
#         self.balans -= summa
#
#
# class JamgArmaMixin:
#     def hisobla_foiz(self):
#         return self.balans * self.foiz_stavka / 100
#
#
# class KreditMixin:
#     def chiqim(self, summa):
#         if self.balans - summa >= -self.limit:
#             self.balans -= summa
#         else:
#             print("Kredit limiti oshib ketdi!")
#
#
# class VipHisob(JamgArmaMixin, KreditMixin, Hisob):
#     def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
#         super().__init__(raqam, egasi, balans)
#         self.foiz_stavka = foiz_stavka
#         self.limit = limit
#
#
# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.egasi = egasi
#         self.balans = balans
#
#     def kirim(self, summa):
#         self.balans += summa
#
#     def chiqim(self, summa):
#         self.balans -= summa
#
#
# class JamgArmaMixin:
#     def hisobla_foiz(self):
#         return self.balans * self.foiz_stavka / 100
#
#
# class KreditMixin:
#     def chiqim(self, summa):
#         if self.balans - summa >= -self.limit:
#             self.balans -= summa
#         else:
#             print("Kredit limiti oshib ketdi!")
#
#
# class VipHisob(JamgArmaMixin, KreditMixin, Hisob):
#     def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
#         super().__init__(raqam, egasi, balans)
#         self.foiz_stavka = foiz_stavka
#         self.limit = limit
#
#
# v = VipHisob("001", "Amirxon", 2_000_000, foiz_stavka=12, limit=500_000)
#
# v.chiqim(10000000)
# print(v.balans)

# # 7-masala
# class Kurs:
#     def __init__(self, nom, davomiylik_hafta, narx):
#         self.nom = nom
#         self.davomiylik_hafta = davomiylik_hafta
#         self.narx = narx
#
#     def malumot(self):
#         return f"Kurs: {self.nom}, Davomiylik: {self.davomiylik_hafta} hafta, Narx: {self.narx}"
#
#
# class OnlaynKurs(Kurs):
#     def __init__(self, nom, davomiylik_hafta, narx, platforma):
#         super().__init__(nom, davomiylik_hafta, narx)
#         self.platforma = platforma
#
#     def malumot(self):
#         m = super().malumot()
#         return f"{m}, Platforma: {self.platforma}"
#
#
# class OfflineKurs(Kurs):
#     def __init__(self, nom, davomiylik_hafta, narx, manzil):
#         super().__init__(nom, davomiylik_hafta, narx)
#         self.manzil = manzil
#
#     def malumot(self):
#         x = super().malumot()
#         return f"{x}, Manzil: {self.manzil}"
#
#
# kurslar = [
#     OnlaynKurs("Python", 12, 1_800_000, "Coursera"),
#     OfflineKurs("Kiberxavfsizlik", 40, 25_000_000, "Toshkent")
# ]
#
# for kurs in kurslar:
#     print(kurs.malumot())

# # 8-masala
# class taom:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def tavsif(self):
#         return "Taom: {nom}, Narx: {narx}"
#
# class IssiqTaom(taom):
#     def __init__(self, nom, narx, kaloriya):
#         super().__init__(nom, narx)
#         self.kaloriya = kaloriya
#
#     def tavsif(self):
#         b = super().tavsif()
#         return f"{b}, Kaloriya: {self.kaloriya}"
#
# class Ichimlik(taom):
#     def __init__(self, nom, narx, kaloriya, hajm_ml):
#         super().__init__(self, nom,narx, kaloriya)
#         self.hajm_ml = hajm_ml
#
#     def tavsif(self):
#             x = super().tavsif()
#             return f"{x}, Hajm_ml: {self.hajm_ml}"
#
#     def chegirma_qollash(taomlar, foiz):
#         return foiz
#
# isiqt = IssiqTaom("Kozonkabob", "200", "300", "0.5")
# ich = Ichimlik("Cola", "20", "100", "2.5 l")
#
# print(isiqt)
# print(ich)

# # 9-masala
# from abc import ABC, abstractmethod
# from typing import List
#
#
# class JamoaAzo(ABC):
#     def __init__(self, ism: str) -> None:
#         self.ism = ism
#
#     @abstractmethod
#     def vazifa(self) -> str:
#         """Har bir rol uchun aniq vazifani qaytaradi."""
#         raise NotImplementedError
#
#
# class BackendDasturchi(JamoaAzo):
#     def vazifa(self) -> str:
#         return "API va ma'lumotlar bazasi bilan ishlaydi"
#
#
# class FrontendDasturchi(JamoaAzo):
#     def vazifa(self) -> str:
#         return "UI va foydalanuvchi tajribasini yaratadi"
#
#
# class Tester(JamoaAzo):
#     def vazifa(self) -> str:
#         return "Tizimni test qiladi"
#
#
# def hisobot(azolar: List[JamoaAzo]) -> None:
#     for a in azolar:
#         print(f"Ism: {a.ism}, Vazifa: {a.vazifa()}")
#
# jamoa = [
#         BackendDasturchi("Marjona"),
#         FrontendDasturchi("Maftuna"),
#         Tester("G'anijon"),
#     ]
#
# hisobot(jamoa)


# # 10-masala
# class QadamSanagich:
#     def __init__(self, kunlik_maqsad, qadamlar):
#         self.kunlik_maqsad = kunlik_maqsad
#         self.qadamlar = qadamlar
#
#     def bajarilgan_kunlar(self):
#         return "Nechta kunda maqsad bajarildi!"
#
#     def ortalama_qadam(self):
#         return "o'rtacha kunlik qadamlar!"
#
# class MotivatsionQadamSanagich(QadamSanagich):
#     def motivatsiya_xabari(self):
#         return ""
#
#     def QadamSanagich(self):
#         m = self.motivatsiya_xabari()
#         if m ≥ 5:
#             return "Barakalla! Siz juda faol ekansiz!"
#         return "Harakatni ko'proq oshiring!"
#
# hafta = [10000, 7500, 8200, 9000, 5000, 12000, 8000]
# q = MotivatsionQadamSanagich(8000, hafta)
# print(q.bajarilgan_kunlar())
# print(q.ortalama_qadam())
# print(q.motivatsiya_xabari())