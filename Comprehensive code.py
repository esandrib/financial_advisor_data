from collections import Counter
import xml.etree.ElementTree as ET

tree1 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds1.xml')
tree2 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds2.xml')
tree3 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds3.xml')
tree4 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds4.xml')
tree5 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds5.xml')
tree6 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds6.xml')
tree7 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds7.xml')
tree8 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds8.xml')
tree9 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds9.xml')
tree10 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds10.xml')
tree11 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds11.xml')
tree12 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds12.xml')
tree13 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds13.xml')
tree14 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds14.xml')
tree15 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds15.xml')
tree16 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds16.xml')
tree17 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds17.xml')
tree18 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds18.xml')
tree19 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds19.xml')
tree20 = ET.parse(r'C:\Users\ESandrib\AppData\Local\Temp\Temp1_IA_INDVL_Feed_04_10_2021.xml.zip\IA_Indvl_Feeds20.xml')
#root = tree.getroot()


results1 = []

for indvls in tree1.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results1.append(ress)

results2 = []

for indvls in tree2.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results2.append(ress)

results3 = []

for indvls in tree3.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results3.append(ress)
results4 = []

for indvls in tree4.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results4.append(ress)
results5 = []

for indvls in tree5.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results5.append(ress)
results6 = []

for indvls in tree6.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results6.append(ress)
results7 = []

for indvls in tree7.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results7.append(ress)
results8 = []

for indvls in tree8.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results8.append(ress)
results9 = []

for indvls in tree9.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results9.append(ress)
results10 = []

for indvls in tree10.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results10.append(ress)
results11 = []

for indvls in tree11.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results11.append(ress)
results12 = []

for indvls in tree12.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results12.append(ress)
results13 = []

for indvls in tree13.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results13.append(ress)
results14 = []

for indvls in tree14.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results14.append(ress)
results15 = []

for indvls in tree15.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results15.append(ress)
results16 = []

for indvls in tree16.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results16.append(ress)
results17 = []

for indvls in tree17.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results17.append(ress)
results18 = []

for indvls in tree18.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results18.append(ress)
results19 = []

for indvls in tree19.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results19.append(ress)

results20 = []

for indvls in tree20.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasCustComp'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            results20.append(ress)

wells = results1.count('19616') + results2.count('19616') + results3.count('19616') + results4.count('19616') + results5.count('19616') + results6.count('19616') + results7.count('19616') + results8.count('19616') + results9.count('19616') + results10.count('19616') + results11.count('19616') + results12.count('19616') + results13.count('19616') + results14.count('19616') + results15.count('19616') + results16.count('19616') + results17.count('19616') + results18.count('19616') + results19.count('19616')+ results20.count('149777')
merrill = results1.count('7691') + results2.count('7691') + results3.count('7691') + results4.count('7691') + results5.count('7691') + results6.count('7691') + results7.count('7691') + results8.count('7691') + results9.count('7691') + results10.count('7691') + results11.count('7691') + results12.count('7691') + results13.count('7691') + results14.count('7691') + results15.count('7691') + results16.count('7691') + results17.count('7691') + results18.count('7691') + results19.count('7691')+ results20.count('149777')
ubs = results1.count('8174') + results2.count('8174') + results3.count('8174') + results4.count('8174') + results5.count('8174') + results6.count('8174') + results7.count('8174') + results8.count('8174') + results9.count('8174') + results10.count('8174') + results11.count('8174') + results12.count('8174') + results13.count('8174') + results14.count('8174') + results15.count('8174') + results16.count('8174') + results17.count('8174') + results18.count('8174') + results19.count('8174')+ results20.count('149777')
morgan = results1.count('149777') + results2.count('149777') + results3.count('149777') + results4.count('149777') + results5.count('149777') + results6.count('149777') + results7.count('149777') + results8.count('149777') + results9.count('149777') + results10.count('149777') + results11.count('149777') + results12.count('149777') + results13.count('149777') + results14.count('149777') + results15.count('149777') + results16.count('149777') + results17.count('149777') + results18.count('149777') + results19.count('149777') + results20.count('149777')


print("Wells Fargo Has Customer Complaint:", wells)
print("Merrill Has Customer Complaint:",merrill)
print("UBS Has Customer Complaint:",ubs)
print("Morgan Has Customer Complaint:",morgan)

tcustcomp = results1 + results2 + results3 + results4 + results5 + results6 + results7 + results8 + results9 + results10 + results11 + results12 + results13 + results14 + results15 + results16 + results17 + results18 + results19 + results20
tcc = Counter(tcustcomp)
print(tcc)


Term1 = []

for indvls in tree1.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term1.append(ress)

Term2 = []

for indvls in tree2.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term2.append(ress)

Term3 = []

for indvls in tree3.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term3.append(ress)
Term4 = []

for indvls in tree4.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term4.append(ress)
Term5 = []

for indvls in tree5.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term5.append(ress)
Term6 = []

for indvls in tree6.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term6.append(ress)
Term7 = []

for indvls in tree7.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term7.append(ress)
Term8 = []

for indvls in tree8.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term8.append(ress)
Term9 = []

for indvls in tree9.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term9.append(ress)
Term10 = []

for indvls in tree10.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term10.append(ress)
Term11 = []

for indvls in tree11.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term11.append(ress)
Term12 = []

for indvls in tree12.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term12.append(ress)
Term13 = []

for indvls in tree13.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term13.append(ress)
Term14 = []

for indvls in tree14.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term14.append(ress)
Term15 = []

for indvls in tree15.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term15.append(ress)
Term16 = []

for indvls in tree16.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term16.append(ress)
Term17 = []

for indvls in tree17.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term17.append(ress)
Term18 = []

for indvls in tree18.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term18.append(ress)
Term19 = []

for indvls in tree19.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term19.append(ress)

Term20 = []

for indvls in tree20.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasTermination'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            Term20.append(ress)


wellsterm = Term1.count('19616') + Term2.count('19616') + Term3.count('19616') + Term4.count('19616') + Term5.count('19616') + Term6.count('19616') + Term7.count('19616') + Term8.count('19616') + Term9.count('19616') + Term10.count('19616') + Term11.count('19616') + Term12.count('19616') + Term13.count('19616') + Term14.count('19616') + Term15.count('19616') + Term16.count('19616') + Term17.count('19616') + Term18.count('19616') + Term19.count('19616')+ Term20.count('149777')
merrillterm = Term1.count('7691') + Term2.count('7691') + Term3.count('7691') + Term4.count('7691') + Term5.count('7691') + Term6.count('7691') + Term7.count('7691') + Term8.count('7691') + Term9.count('7691') + Term10.count('7691') + Term11.count('7691') + Term12.count('7691') + Term13.count('7691') + Term14.count('7691') + Term15.count('7691') + Term16.count('7691') + Term17.count('7691') + Term18.count('7691') + Term19.count('7691')+ Term20.count('149777')
ubsterm = Term1.count('8174') + Term2.count('8174') + Term3.count('8174') + Term4.count('8174') + Term5.count('8174') + Term6.count('8174') + Term7.count('8174') + Term8.count('8174') + Term9.count('8174') + Term10.count('8174') + Term11.count('8174') + Term12.count('8174') + Term13.count('8174') + Term14.count('8174') + Term15.count('8174') + Term16.count('8174') + Term17.count('8174') + Term18.count('8174') + Term19.count('8174')+ Term20.count('149777')
morganterm = Term1.count('149777') + Term2.count('149777') + Term3.count('149777') + Term4.count('149777') + Term5.count('149777') + Term6.count('149777') + Term7.count('149777') + Term8.count('149777') + Term9.count('149777') + Term10.count('149777') + Term11.count('149777') + Term12.count('149777') + Term13.count('149777') + Term14.count('149777') + Term15.count('149777') + Term16.count('149777') + Term17.count('149777') + Term18.count('149777') + Term19.count('149777') + Term20.count('149777')


print("Wells Fargo Has Termination:", wellsterm)
print("Merrill Has Termination:",merrillterm)
print("UBS Has Termination:",ubsterm)
print("Morgan Has Termination:",morganterm)

tterm = Term1 + Term2 + Term3 + Term4 + Term5 + Term6 + Term7 + Term8 + Term9 + Term10 + Term11 + Term12 + Term13 + Term14 + Term15 + Term16 + Term17 + Term18 + Term19 + Term20
tterms = Counter(tterm)
print(tterms)

invstgn1 = []

for indvls in tree1.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn1.append(ress)

invstgn2 = []

for indvls in tree2.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn2.append(ress)

invstgn3 = []

for indvls in tree3.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn3.append(ress)
invstgn4 = []

for indvls in tree4.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn4.append(ress)
invstgn5 = []

for indvls in tree5.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn5.append(ress)
invstgn6 = []

for indvls in tree6.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn6.append(ress)
invstgn7 = []

for indvls in tree7.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn7.append(ress)
invstgn8 = []

for indvls in tree8.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn8.append(ress)
invstgn9 = []

for indvls in tree9.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn9.append(ress)
invstgn10 = []

for indvls in tree10.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn10.append(ress)
invstgn11 = []

for indvls in tree11.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn11.append(ress)
invstgn12 = []

for indvls in tree12.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn12.append(ress)
invstgn13 = []

for indvls in tree13.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn13.append(ress)
invstgn14 = []

for indvls in tree14.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn14.append(ress)
invstgn15 = []

for indvls in tree15.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn15.append(ress)
invstgn16 = []

for indvls in tree16.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn16.append(ress)
invstgn17 = []

for indvls in tree17.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn17.append(ress)
invstgn18 = []

for indvls in tree18.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn18.append(ress)
invstgn19 = []

for indvls in tree19.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn19.append(ress)

invstgn20 = []

for indvls in tree20.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasInvstgn'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            invstgn20.append(ress)


wellsinvstgn = invstgn1.count('19616') + invstgn2.count('19616') + invstgn3.count('19616') + invstgn4.count('19616') + invstgn5.count('19616') + invstgn6.count('19616') + invstgn7.count('19616') + invstgn8.count('19616') + invstgn9.count('19616') + invstgn10.count('19616') + invstgn11.count('19616') + invstgn12.count('19616') + invstgn13.count('19616') + invstgn14.count('19616') + invstgn15.count('19616') + invstgn16.count('19616') + invstgn17.count('19616') + invstgn18.count('19616') + invstgn19.count('19616')+ invstgn20.count('149777')
merrillinvstgn = invstgn1.count('7691') + invstgn2.count('7691') + invstgn3.count('7691') + invstgn4.count('7691') + invstgn5.count('7691') + invstgn6.count('7691') + invstgn7.count('7691') + invstgn8.count('7691') + invstgn9.count('7691') + invstgn10.count('7691') + invstgn11.count('7691') + invstgn12.count('7691') + invstgn13.count('7691') + invstgn14.count('7691') + invstgn15.count('7691') + invstgn16.count('7691') + invstgn17.count('7691') + invstgn18.count('7691') + invstgn19.count('7691')+ invstgn20.count('149777')
ubsinvstgn = invstgn1.count('8174') + invstgn2.count('8174') + invstgn3.count('8174') + invstgn4.count('8174') + invstgn5.count('8174') + invstgn6.count('8174') + invstgn7.count('8174') + invstgn8.count('8174') + invstgn9.count('8174') + invstgn10.count('8174') + invstgn11.count('8174') + invstgn12.count('8174') + invstgn13.count('8174') + invstgn14.count('8174') + invstgn15.count('8174') + invstgn16.count('8174') + invstgn17.count('8174') + invstgn18.count('8174') + invstgn19.count('8174')+ invstgn20.count('149777')
morganinvstgn = invstgn1.count('149777') + invstgn2.count('149777') + invstgn3.count('149777') + invstgn4.count('149777') + invstgn5.count('149777') + invstgn6.count('149777') + invstgn7.count('149777') + invstgn8.count('149777') + invstgn9.count('149777') + invstgn10.count('149777') + invstgn11.count('149777') + invstgn12.count('149777') + invstgn13.count('149777') + invstgn14.count('149777') + invstgn15.count('149777') + invstgn16.count('149777') + invstgn17.count('149777') + invstgn18.count('149777') + invstgn19.count('149777') + invstgn20.count('149777')


print("Wells Fargo Has Investigation:", wellsinvstgn)
print("Merrill Has Investigation:",merrillinvstgn)
print("UBS Has Investigation:",ubsinvstgn)
print("Morgan Has Investigation:",morganinvstgn)


tinvstgn = invstgn1 + invstgn2 + invstgn3 + invstgn4 + invstgn5 + invstgn6 + invstgn7 + invstgn8 + invstgn9 + invstgn10 + invstgn11 + invstgn12 + invstgn13 + invstgn14 + invstgn15 + invstgn16 + invstgn17 + invstgn18 + invstgn19 + invstgn20
ttinvstgn = Counter(tinvstgn)
print(ttinvstgn)


regact1 = []

for indvls in tree1.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact1.append(ress)

regact2 = []

for indvls in tree2.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact2.append(ress)

regact3 = []

for indvls in tree3.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact3.append(ress)
regact4 = []

for indvls in tree4.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact4.append(ress)
regact5 = []

for indvls in tree5.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact5.append(ress)
regact6 = []

for indvls in tree6.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact6.append(ress)
regact7 = []

for indvls in tree7.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact7.append(ress)
regact8 = []

for indvls in tree8.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact8.append(ress)
regact9 = []

for indvls in tree9.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact9.append(ress)
regact10 = []

for indvls in tree10.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact10.append(ress)
regact11 = []

for indvls in tree11.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact11.append(ress)
regact12 = []

for indvls in tree12.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact12.append(ress)
regact13 = []

for indvls in tree13.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact13.append(ress)
regact14 = []

for indvls in tree14.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact14.append(ress)
regact15 = []

for indvls in tree15.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact15.append(ress)
regact16 = []

for indvls in tree16.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact16.append(ress)
regact17 = []

for indvls in tree17.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact17.append(ress)
regact18 = []

for indvls in tree18.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact18.append(ress)
regact19 = []

for indvls in tree19.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact19.append(ress)

regact20 = []

for indvls in tree20.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):

        for drps in indvl.findall('DRPs'):

            for drp in drps.findall('DRP'):

                for find in drp.get('hasRegAction'):
                    if find == 'Y':

                        for res in indvl.findall('./CrntEmps/CrntEmp'):

                            ress = res.get('orgPK')
                            regact20.append(ress)

wellsregact = regact1.count('19616') + regact2.count('19616') + regact3.count('19616') + regact4.count('19616') + regact5.count('19616') + regact6.count('19616') + regact7.count('19616') + regact8.count('19616') + regact9.count('19616') + regact10.count('19616') + regact11.count('19616') + regact12.count('19616') + regact13.count('19616') + regact14.count('19616') + regact15.count('19616') + regact16.count('19616') + regact17.count('19616') + regact18.count('19616') + regact19.count('19616')+ regact20.count('149777')
merrillregact = regact1.count('7691') + regact2.count('7691') + regact3.count('7691') + regact4.count('7691') + regact5.count('7691') + regact6.count('7691') + regact7.count('7691') + regact8.count('7691') + regact9.count('7691') + regact10.count('7691') + regact11.count('7691') + regact12.count('7691') + regact13.count('7691') + regact14.count('7691') + regact15.count('7691') + regact16.count('7691') + regact17.count('7691') + regact18.count('7691') + regact19.count('7691')+ regact20.count('149777')
ubsregact = regact1.count('8174') + regact2.count('8174') + regact3.count('8174') + regact4.count('8174') + regact5.count('8174') + regact6.count('8174') + regact7.count('8174') + regact8.count('8174') + regact9.count('8174') + regact10.count('8174') + regact11.count('8174') + regact12.count('8174') + regact13.count('8174') + regact14.count('8174') + regact15.count('8174') + regact16.count('8174') + regact17.count('8174') + regact18.count('8174') + regact19.count('8174')+ regact20.count('149777')
morganregact = regact1.count('149777') + regact2.count('149777') + regact3.count('149777') + regact4.count('149777') + regact5.count('149777') + regact6.count('149777') + regact7.count('149777') + regact8.count('149777') + regact9.count('149777') + regact10.count('149777') + regact11.count('149777') + regact12.count('149777') + regact13.count('149777') + regact14.count('149777') + regact15.count('149777') + regact16.count('149777') + regact17.count('149777') + regact18.count('149777') + regact19.count('149777') + regact20.count('149777')

print("Wells Fargo Has Regulatory Action:", wellsregact)
print("Merrill Has Regulatory Action:",merrillregact)
print("UBS Has Regulatory Action:",ubsregact)
print("Morgan Has Regulatory Action:",morganregact)

tregact = regact1 + regact2 + regact3 + regact4 + regact5 + regact6 + regact7 + regact8 + regact9 + regact10 + regact11 + regact12 + regact13 + regact14 + regact15 + regact16 + regact17 + regact18 + regact19 + regact20
ttregact = Counter(tregact)
print(ttregact)

org1 = []

for indvls in tree1.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org1.append(orgg)

org2 = []

for indvls in tree2.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org2.append(orgg)

org3 = []

for indvls in tree3.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org3.append(orgg)

org4 = []

for indvls in tree4.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org4.append(orgg)

org5 = []

for indvls in tree5.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org5.append(orgg)

org6 = []

for indvls in tree6.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org6.append(orgg)

org7 = []

for indvls in tree7.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org7.append(orgg)

org8 = []

for indvls in tree8.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org8.append(orgg)

org9 = []

for indvls in tree9.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org9.append(orgg)

org10 = []

for indvls in tree10.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org10.append(orgg)

org11 = []

for indvls in tree11.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org11.append(orgg)

org12 = []

for indvls in tree12.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org12.append(orgg)

org13 = []

for indvls in tree13.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org13.append(orgg)

org14 = []

for indvls in tree14.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org14.append(orgg)

org15 = []

for indvls in tree15.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org15.append(orgg)

org16 = []

for indvls in tree16.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org16.append(orgg)

org17 = []

for indvls in tree17.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org17.append(orgg)

org18 = []

for indvls in tree18.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org18.append(orgg)

org19 = []

for indvls in tree19.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org19.append(orgg)

org20 = []

for indvls in tree20.findall('Indvls'):
    for indvl in indvls.findall('Indvl'):
        for numorg in indvl.findall('./CrntEmps/CrntEmp'):

            orgg = numorg.get('orgPK')
            org20.append(orgg)



wellst = org1.count('19616') + org2.count('19616') + org3.count('19616') + org4.count('19616') + org5.count('19616') + org6.count('19616') + org7.count('19616') + org8.count('19616') + org9.count('19616') + org10.count('19616') + org11.count('19616') + org12.count('19616') + org13.count('19616') + org14.count('19616') + org15.count('19616') + org16.count('19616') + org17.count('19616') + org18.count('19616') + org19.count('19616')+ org20.count('149777')
merrillt = org1.count('7691') + org2.count('7691') + org3.count('7691') + org4.count('7691') + org5.count('7691') + org6.count('7691') + org7.count('7691') + org8.count('7691') + org9.count('7691') + org10.count('7691') + org11.count('7691') + org12.count('7691') + org13.count('7691') + org14.count('7691') + org15.count('7691') + org16.count('7691') + org17.count('7691') + org18.count('7691') + org19.count('7691')+ org20.count('149777')
ubst = org1.count('8174') + org2.count('8174') + org3.count('8174') + org4.count('8174') + org5.count('8174') + org6.count('8174') + org7.count('8174') + org8.count('8174') + org9.count('8174') + org10.count('8174') + org11.count('8174') + org12.count('8174') + org13.count('8174') + org14.count('8174') + org15.count('8174') + org16.count('8174') + org17.count('8174') + org18.count('8174') + org19.count('8174')+ org20.count('149777')
morgant = org1.count('149777') + org2.count('149777') + org3.count('149777') + org4.count('149777') + org5.count('149777') + org6.count('149777') + org7.count('149777') + org8.count('149777') + org9.count('149777') + org10.count('149777') + org11.count('149777') + org12.count('149777') + org13.count('149777') + org14.count('149777') + org15.count('149777') + org16.count('149777') + org17.count('149777') + org18.count('149777') + org19.count('149777') + org20.count('149777')



print("Wells Fargo Total", wellst)
print("Merrill Total", merrillt)
print("UBS Total", ubst)
print("Morgan Total", morgant)


torg = org1 + org2 + org3 + org4 + org5 + org6 + org7 + org8 + org9 + org10 + org11 + org12 + org13 + org14 + org15 + org16 + org17 + org18 + org19 + org20
ttorg = Counter(torg)
print(len(torg))


#rezults = []

#for indvls in tree.findall('Indvls'):
    #for indvl in indvls.findall('Indvl'):

        #for drps in indvl.findall('DRPs'):

            #for drp in drps.findall('DRP'):

                #for find in drp.get('hasCustComp'):
                    #if find == 'Y':

                        #for rez in indvl.findall('./CrntEmps/CrntEmp'):

                            #rezz = rez.get('orgNm')
                            #rezults.append(rezz)


#Wells: 19616
#MERRILL: 7691
#UBS: 8174
#Morgan Staney: 149777




#find occurences of part of string
#op = sum("MERRILL" in s for s in rezults)




