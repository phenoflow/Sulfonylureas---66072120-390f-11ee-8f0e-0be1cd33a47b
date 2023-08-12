# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"17343","system":"gprdproduct"},{"code":"21564","system":"gprdproduct"},{"code":"29939","system":"gprdproduct"},{"code":"31212","system":"gprdproduct"},{"code":"32","system":"gprdproduct"},{"code":"34399","system":"gprdproduct"},{"code":"34932","system":"gprdproduct"},{"code":"36856","system":"gprdproduct"},{"code":"42790","system":"gprdproduct"},{"code":"43065","system":"gprdproduct"},{"code":"45215","system":"gprdproduct"},{"code":"48056","system":"gprdproduct"},{"code":"51955","system":"gprdproduct"},{"code":"54764","system":"gprdproduct"},{"code":"55862","system":"gprdproduct"},{"code":"56008","system":"gprdproduct"},{"code":"60495","system":"gprdproduct"},{"code":"61957","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('sulfonylureas-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["sulfonylureas-gliclazide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["sulfonylureas-gliclazide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["sulfonylureas-gliclazide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
