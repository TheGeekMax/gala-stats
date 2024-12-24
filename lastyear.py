class Commande:
    def __init__(self, reference_commande, date_commande, statut_commande, nom_participant, prenom_participant, nom_payeur, prenom_payeur, email_payeur, raison_sociale, moyen_paiement, billet, numero_billet, tarif, montant_tarif, code_promo, montant_code_promo):
        self.reference_commande = reference_commande
        self.date_commande = date_commande
        self.statut_commande = statut_commande
        self.nom_participant = nom_participant
        self.prenom_participant = prenom_participant
        self.nom_payeur = nom_payeur
        self.prenom_payeur = prenom_payeur
        self.email_payeur = email_payeur
        self.raison_sociale = raison_sociale
        self.moyen_paiement = moyen_paiement
        self.billet = billet
        self.numero_billet = numero_billet
        self.tarif = tarif
        self.montant_tarif = montant_tarif
        self.code_promo = code_promo
        self.montant_code_promo = montant_code_promo

    def __repr__(self):
        return f"Commande({self.reference_commande}, {self.date_commande}, {self.statut_commande}, {self.nom_participant}, {self.prenom_participant}, {self.nom_payeur}, {self.prenom_payeur}, {self.email_payeur}, {self.raison_sociale}, {self.moyen_paiement}, {self.billet}, {self.numero_billet}, {self.tarif}, {self.montant_tarif}, {self.code_promo}, {self.montant_code_promo})"

datas = []

with open('gala2023.csv', 'r') as f:
    next(f)
    for line in f:
        data = line.strip().split(';')
        datas.append(Commande(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15]))

TARIF_NORMAL = "Tarif normal"
TARIF_COTISANT = "Tarif réduit 2 : Cotisants du BDE de l’ENSISA"
TARIF_ETUDIANT = "Tarif alternatif : anciens de l'ENSISA"
TARIF_ALUMNIS = "Tarif réduit 1 : étudiants de l’ENSISA"

date_list = {}

for data in datas:
    if data.tarif in [TARIF_NORMAL, TARIF_COTISANT, TARIF_ETUDIANT, TARIF_ALUMNIS]:
        date = data.date_commande.split(' ')[0]
        if date not in date_list:
            date_list[date] = 0
        date_list[date] += 1

import matplotlib.pyplot as plt

print(date_list)
#x rotation
plt.xticks(rotation=90)
plt.bar([d.split("/")[0]+"/"+d.split("/")[1] for d in date_list.keys()], date_list.values())
plt.show()

