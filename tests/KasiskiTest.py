import unittest
from vigenere.Kasiski import computeKeyLength

'''
Kasiski examination test

@author: gbabin
'''

class KasiskiTestCase(unittest.TestCase):

    def test_1(self):
        # https://fr.wikipedia.org/wiki/Cryptanalyse_du_chiffre_de_Vigenère
        text = ('KQOWEFVJPUJUUNUKGLMEKJINMWUXFQMKJBGWRLFNFGHUDWUUMBSVLPS'
                'NCMUEKQCTESWREEKOYSSIWCTUAXYOTAPXPLWPNTCGOJBGFQHTDWXIZA'
                'YGFFNSXCSEYNCTSSPNTUJNYTGGWZGRWUUNEJUUQEAPYMEKQHUIDUXFP'
                'GUYTSMTFFSHNUOCZGMRUWEYTRGKMEEDCTVRECFBDJQCUSWVBPNLGOYL'
                'SKMTEFVJJTWWMFMWPNMEMTMHRSPXFSSKFFSTNUOCZGMDOEOYEEKCPJR'
                'GPMURSKHFRSEIUEVGOYCWXIZAYGOSAANYDOEOYJLWUNHAMEBFELXYVL'
                'WNOJNSIOFRWUCCESWKVIDGMUCGOCRUWGNMAAFFVNSIUDEKQHCEUCPFC'
                'MPVSUDGAVEMNYMAMVLFMAOYFNTQCUAFVFJNXKLNEIWCWODCCULWRIFT'
                'WGMUSWOVMATNYBUHTCOCWFYTNMGYTQMKBBNLGFBTWOJFTWGNTEJKNEE'
                'DCLDHWTYYIDGMVRDGMPLSWGJLAGOEEKJOFEKUYTAANYTDWIYBNLNYNP'
                'WEBFNLFYNAJEBFR')

        self.assertEqual(computeKeyLength(text), 5)


    def test_2(self):
        # http://www.cs.trincoll.edu/~crypto/historical/vigenere.html
        text = ('KSMEHZBBLKSMEMPOGAJXSEJCSFLZSY')

        self.assertEqual(computeKeyLength(text), 9)


    def test_3(self):
        # Nuit du hack 2011 : CTF-prequal, crypto lvl 1
        text = ('nfptfwawmgsscqyamgcdciwittwfaievlauhggygmicmwhigfpzmuhc'
                'kkplglzwhtrrvparrelpctgphjbdrtwzzmfwjgpviwmkoaxikjqifpv'
                'acxefikuemvppxwhoescvjtzsgjwmqsctgckcsnwdykwxtzvazmfvzo'
                'jxbpumybyjgbmxvcdkpzbljswxpzupapnelqsboxwmmeiefpawrutca'
                'xftwiotpveacwnttsjmalwkursexhtpvuvqiloamwhtvrvbbxvptgsn'
                'bepgltqrnpyynozbpmdsekyapluhzghckcabhxeyhphfplkerpvycos'
                'yifuimjgacvacdmcmsdimmthcgjbyforsgbgdgwftvzuxcifkkntwsd'
                'ivyiwluwmrqkjqtnhqijgtrkwtagrnvpxlefiwnsmtvbuwgxfjjmdlx'
                'vcvrzuzqqnpkccnbnqgfamjgyixfgdgskwdykgpyikzxvbkenghwysv'
                'cdrvewpeegkppgcytjyimlowwvgcdcingasjnpeiebqhqqcmgvcctgl'
                'xwcgvnvvpxgaeolzwbxglnhdsywknpmhppdohqfnsqwngecpgoaijnd'
                'vkqyksafzktghfqficmdrlzhvgkycmspwluamhwlbteqzbtghtrlygh'
                'loacvckjhjlhzmhmjqdcnverwcgqxfzwankmkclihvcddtnutelztpz'
                'uuqfuhraxewdmkpjpgwaixrulqrbdtxnyciecaqwhncybvcctwlkmkc'
                'lmkrvecfnsgiknxflnbupnelqtkoeqghiijullhnrzzjlefmkmthffp'
                'wmavvetkqzrmvxeuqumgrpzkjmalyjchsiepuehtzqcbpspswjwukhu'
                'ihckybxhxmdyrxluhuiggegboweewjthvubagvrzrqeoyhanbecgzce'
                'qcgcaesyxwmfyvkuwvacicbngnvsmvvrxplefkkcvxhqidchazupcpg'
                'tzaxxgtrkyselibmhvieghlwxqsftwlckiwnizribgdmlyvijvhawbf'
                'rjtlqzryotgfotwhbkertzscumchzzvhmhveksbhrtswntxrfhlmckj'
                'axguaskotvvuvleygjzatbomlcxwnkzqitgkljezlsjwxjlujmqbtsg'
                'fnwdqgfamjcucrpcvlttbtrdcvyccxcmfofjabgeidfjwawzbsrivrg'
                'nhcyeoihziuqwfkdrxgqthmhihlkzdiageyibgdehctrjcwqianzrdk'
                'odykjtrukzaictvrxnadivjtrrvpjyfofjtlhtimfivzelazhngsith'
                'prghjxvtvaxrogshnzevawxijopmxnovrbbjzpmneekckqtvutgczsc'
                'elwdruktmrgwdldgjppncievkhkyykjldgefmkcchziuqwfkdojtatr'
                'nyhxzdbtyzuvbutinmtohjrwjqfhumgktafwkohgzrpbtegkgjfbfpd'
                'uhegklvmqslghjipjwlbievbuqvvvkehfxekmpqvvbaygfrnxuidsjh'
                'pvvpbvgikkytbddyeyamkdpjiaflkxwftwmmbeltpamafzybiccxlci'
                'sigywwfevjtkwdumykicxpdezwjgsbbnsfmtgkgaciecvlttbomunjq'
                'rpamigorsgbgtrmnxrmgszmfwjktmidiyyiicgpniafhspfdppdycxv'
                'uxcirtrrkbhlisgtxewstenovrlbgtpwwiyjtpayfuvbikwdxakjiec'
                'awuhglrekopwwhimlokqkakjqxfqzqeisskcjqxvgxchmodpswjwjwz'
                'xiafzqhxwyxwatvmqscxcckftgrcijciwfnsqgvvlbxgofkmytvfusm'
                'sygfnatqpvsnlmjkucpycesaeoxrmfaewgyuiavlkknzayluiiequvy'
                'ynrkehgfijysegkicwzcjqpgiwpsgxrgjhaiynlqtnieylmdpckjqxh'
                'fzlhtutxlchetuluihkjkdwaliuycejguqqwwjrdtqthniaykrhbmau'
                'vbhxbpglohwrgwmqnwighfofvamiicnbawrfdyvgoweuohrlpjqrgct'
                'gibglkanimjjlvhegigioweewhxfyrvzxgkkmgtqweuccmrwsbvvevq'
                'rhbomeycxlosmggwjljgqdeycixzuypsaelqtmbpumyuetksqwvurlx'
                'lznsfmtulcabmaezbjgheidfjwmgzbmowcsbmswpmmtpvkmmrqpljat'
                'gtxnyaicgtmrgwdzxusyhmgaetwzmyvudmsxzpqwhiydcuwrhodwjeh'
                'cmuyhedgaxlntvrgtjprwhpxzuswvrolrpghprghyyjvvqrigcndkhl'
                'emajiuqumgfwjaxiwepgvdvkkzmyzclpxlhcmknxulghtmdwvrbtuye'
                'uogeskacvfkkjdksxtwfaievlauhgvjxmqfvsvxxltpvxrivppnufia'
                'huetksqwvuvppmcomggpyikzayfrvlsbgdiwatxzpamkrtjcfnwaifu'
                'imswzihzktppltcmfaxpccsigvpzyrhaxsviamxwsizrnzrteweeeyi'
                'rzusvipcktteowmiopqckncpnuvbkxzdiegpyikzdiywcjpfqzvhygh'
                'fnvzhvcdljezlilmtqmgzbmowcsblwezwfxxegjtipvlqjmrzrwwxrd'
                'clkiacjpxlidxwgesievuqbffltvsemsgeycxpveedcycwweylxxwaw'
                'zbsekjshvcywwkjekppjlfgubjbgxeyhxwcgjbyffzainaavsyhievy'
                'qwhujshisyhamhiwcjqpvuzyrvixwshelrultphulrpwoamtohhlkzv'
                'ezcdcithbywurrfphbepflgheonykhtggjhaiynlqgbgfwvyaitvbar'
                'vdytxooxykhtgrnpyynohspfgphhbpvvvyimahvsvboemfntvuwtixr'
                'vvrxgjppvcvrzuzqqnovrktftykhxfyypamywtrjljfphoiekgtiwfc'
                'gmgmogejcjwffpwzrnugvgwdwagtkvuaiwnwtrdkjpvgxdrvewtepgi'
                'yiifzmflxhzebtyfjvlskscmlpjpgwaixryzqxtapxeuixzuloifvrq'
                'ihfesjnjvgkzcxewkpjfbpg')

        self.assertEqual(computeKeyLength(text), 18)


    def test_4(self):
        # Nuit du hack 2013 : Public Wargame
        text = ('xpascibmnbusrejctwvkzwvftnhrqdiktmvrhoihzutjqwxcbitrwyk'
                'odlejrkhruzrksttudsskzxtmfnfiimnozravemstfmjbgoqelfhksh'
                'setvaiaifnidioeoyfjgkjfofuyssxkyawkwswoxbbmjgfvexetlssy'
                'kaioiemnbwviwixdilodxczkhtooequhyhkhzjeubtpdlngktssjamc'
                'rqxcexitsmwsjkmwhytamgalgjzxipxyeupxzxylnmnfiewmdrrindo'
                'hkifrhwqekralqghyfhytzojpoaghpyspfwtwqwizfyqsstifuohxik'
                'rtiinzrjskgoikiwgdosjyhfvkmmngdimogeqtsmsfqikymavkplkif'
                'mvbdhqkxkiicsfrvwmdrpledrgcvlnfmenvglusykzuinrrngdvslal'
                'rpuhiejzzgethobxfmnbusrejcvptjsiwypvaiguqkxzwrhfjecqghs'
                'zylykvgbzfshmcslwalwgtfqonaalpdwlvmsntfovdtzrcxhscolwog'
                'cfkuwqllhvvvewwuarsjbagnxuyojtyjzoitxfbyqgbkxztsfxqxafa'
                'hyvogrsefnbzpppyjdphlhmolagizripbwqhsrcjwiaifkzklkmzedm'
                'qxtucjidewzsbciymprovrmpmofikfmpustqrefgzbekzmvmoiantft'
                'cfqixabtkxhytkhhvikwwpppnpviixxhlwkbzbzmfoefjlqqaxdikoi'
                'mqifhpggujclluwsetiqyselamjliipugtikmmkpwmndobreaezuinw'
                'ptspapvfvfbuajfegkkwxykfpzrqiepmoxswsawyizjojktrmpujyst'
                'mcejzqggzssntftcfqixabtspyqqfzoyiyofbjlkgkiynryafkwebze'
                'gfqbwkfagsjkacdlcmfvfmttwbflwuoxvepwpsmzmvhuplizdikmmqm'
                'cinobiaqhasfmslfxvvghztenefufizwtreofqisnjdzvertrswaikx'
                'whmslfxriabfkxjxjihomjpompbbssmnlzwyvyzdsezsivwgslpxukv'
                'vrehunjhkfalxtwnlqqvfummpuvepovpmvmcqsldcvamxscpeuhuelp'
                'uwihhfseuidxqmvawpomxgdwhtkliufvptjsijetxlmhswqxkaveuqi'
                'univhzhepneyjxtrohbxbvlfhorrjgwjasknwulhqxndhtikxfyfelo'
                'hdmxyqsedtcyhecprvecykcxjlvujjpwqeivjlyhafemnecnvxorfew'
                'duhhervuihtjev')

        self.assertEqual(computeKeyLength(text), 45)

    def test_5(self):
        # Nuit du hack 2012 : CTF-prequal, crypto
        text = ('vnrvusqlwqhhdsqhvunqhvwdjkftdmxafxwiqoisxcdldnbeqexzzjx'
                'emyfwiathfsqxojeevashhcvtdscntdfckwmcwynlaghhsllmsxztul'
                'vwcrufbsfbhhgryifoboowfgyngkimvlxoquxugehirqeyiydrcntos'
                'qqoxsyfnlkgrxfqqctjarimrsmqjxbsxoqimgkirudnixkjyyvpebqj'
                'oryxqycbyifvuyayqdnrnvlqqqkbicnwlrdrwvlxoquxyxgueqjhnoh'
                'xtjlrrjaujkpdcdmosxrobwofjmcutnzsfjkvsxbbircrvojhwonurj'
                'eevsbqozwhctleflhsslnsicneersjchpidwruutrxwsqqntjfhhtru'
                'igjlxukrkysrvtsslkzqhrimrdwairefhnbidrwlojbyirrfbtslrrl'
                'dvifkkyinwxoskortwdifgkiafoooxnbingdghchstdxtqohohzynoo'
                'sheorgkifyqfsxchaaglsbqeyiycgisrsmsshccklnxeghwhfuyuwjl'
                'vuvohteucqnyzxhgwtgsldsjtmoiggyvqfuqtvrimrlrqbxnsxrmwlh'
                'giwdfchiuhviafxvyvbczchhenvogvrboujrmwbuhodgziycgyaqgvs'
                'ivsbwjmxtuhwwphsbwuzveydwyfdcgbxqxdvvtzqbkdwxljtzrzzhsg'
                'rrbfwayotfyqdoqunwaghwcchcdfldinfweqavepgbogoiuwdcrfzwb'
                'sxiapsjhuwcakqlengxvuskgxfnldsusaiwnwslzfleherhhchtadnh'
                'rvxosnzcnwsyrnghpisbsydqhrrwsihpkwskzmipdpzowrwxyqigedq'
                'rehcbtcgcntxwsvxvwyrrdufwegqpzzjuzveypewdgsguuzsajhpqep'
                'oajbrugrpsjbugsqlngepdpzfusbyjrefbuedqvcktacwayoegaskgx'
                'fnldqlwdbdigfwdlrbuqclobswanlcnopdhlxhvdhneagxscsbczchh'
                'earxiihnoshlirroepuodsryqiuglrscrfzwokugslpssdvzirrjfvo'
                'iqeqdsscdhdydfsbzozhxlydozizsrwstwrwighiyifsdfmrychuigx'
                'hvzcjkubrotktpcuikofenvisdwofdxtlpnvwdxukgjuzveyhvfeunp'
                'sxoyiglwbewdvjpnidcdwgmrbrcjkubrolwdwnpxlhnernriywnimjb'
                'ecbpporhvtqjfziyhhpuvyoxxdftkw')

        self.assertEqual(computeKeyLength(text), 13)

    def test_6(self):
        # Nuit du hack 2010 : Public Wargame crypto 3
        text = ('wsszdvodgowhooehzbodnsespsaqpigdpgekpaocpqpspleddoyrpga'
                'zns')

        self.assertEqual(computeKeyLength(text), 4)


if __name__ == '__main__':
    unittest.main()
