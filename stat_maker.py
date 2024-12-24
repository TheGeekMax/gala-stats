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

with open('gala.csv', 'r') as f:
    next(f)
    for line in f:
        data = line.strip().split(';')
        datas.append(Commande(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15]))


BOISSON = "Les Jetons Boisson"
TARIF_NORMAL = "Tarif Normal"
TARIF_COTISANT = "Etudiant ENSISA cotisant"
TARIF_ETUDIANT = "Etudiant"
TARIF_ALUMNIS = "Tarif Alumnis"
TOMBOLA = "Ticket de Tombola"

stats_count = {}

money = 0

for data in datas:
    money += float(data.montant_tarif.replace(',', '.'))
    if data.tarif == BOISSON:
        if data.tarif not in stats_count:
            stats_count[data.tarif] = 1
        else:
            stats_count[data.tarif] += 1
    elif data.tarif == TOMBOLA:
        if data.tarif not in stats_count:
            stats_count[data.tarif] = 1
        else:
            stats_count[data.tarif] += 1
    else:
        if data.tarif == TARIF_NORMAL:
            if TARIF_NORMAL not in stats_count:
                stats_count[TARIF_NORMAL] = 1
            else:
                stats_count[TARIF_NORMAL] += 1
            if "Total" not in stats_count:
                stats_count["Total"] = 1
            else:
                stats_count["Total"] += 1
        elif data.tarif == TARIF_COTISANT:
            if TARIF_COTISANT not in stats_count:
                stats_count[TARIF_COTISANT] = 1
            else:
                stats_count[TARIF_COTISANT] += 1
            if "Total" not in stats_count:
                stats_count["Total"] = 1
            else:
                stats_count["Total"] += 1
        elif data.tarif == TARIF_ETUDIANT:
            if TARIF_ETUDIANT not in stats_count:
                stats_count[TARIF_ETUDIANT] = 1
            else:
                stats_count[TARIF_ETUDIANT] += 1
            if "Total" not in stats_count:
                stats_count["Total"] = 1
            else:
                stats_count["Total"] += 1
        elif data.tarif == TARIF_ALUMNIS:
            if TARIF_ALUMNIS not in stats_count:
                stats_count[TARIF_ALUMNIS] = 1
            else:
                stats_count[TARIF_ALUMNIS] += 1
            if "Total" not in stats_count:
                stats_count["Total"] = 1
            else:
                stats_count["Total"] += 1

# export in md format stats
from datetime import datetime
with open('stats.md', 'w') as f:
    # print date in format DD/MM/YYYY
    today = datetime.today()
    f.write("# Stats de la date du " + today.strftime("%d/%m/%Y") + "\n\n")
    f.write("## Billets vendus\n\n")
    f.write("**total**: " + str(stats_count["Total"]) + "\n\n")
    f.write("- Normal: " + str(stats_count[TARIF_NORMAL]) + "\n")
    f.write("- Etudiant ENSISA cotisant: " + str(stats_count[TARIF_COTISANT]) + "\n")
    f.write("- Etudiant: " + str(stats_count[TARIF_ETUDIANT]) + "\n")
    f.write("- Alumnis: " + str(stats_count[TARIF_ALUMNIS]) + "\n\n")
    f.write("## Boissons vendues\n\n")
    f.write("total: " + str(stats_count[BOISSON]) + "\n\n")
    f.write("## Tickets de Tombola vendus\n\n")
    f.write("total: " + str(stats_count[TOMBOLA]) + "\n\n")
    f.write("## Total des ventes\n\n")
    f.write("total: " + str(money) + "€\n\n")