import re

if __name__ == '__main__':
    cookie_str1 = 'hiijack=0; _csrfToken=dxbiTzixDmgmiJFFrZTLt3vbINBhwHESNIijRfld; newstatisticUUID=1610949709_161617074; UM_distinctid=1771415d8a4946-0e97a1d32324cf-31346d-e1000-1771415d8a5987; Hm_lvt_76131d7573faf448cb1cfa2a37e6e3ff=1614334974,1614756983,1615168836,1615261325; Hm_lpvt_76131d7573faf448cb1cfa2a37e6e3ff=1615261334'
    cookie_str2 = 'hiijack=0; _csrfToken=dxbiTzixDmgmiJFFrZTLt3vbINBhwHESNIijRfld; newstatisticUUID=1610949709_161617074; UM_distinctid=1771415d8a4946-0e97a1d32324cf-31346d-e1000-1771415d8a5987; Hm_lvt_76131d7573faf448cb1cfa2a37e6e3ff=1614334974,1614756983,1615168836,1615261325; Hm_lpvt_76131d7573faf448cb1cfa2a37e6e3ff=1615272075'
    cookie_str3 = 'e1={"pid":"qd_P_xiangqing","eid":"","l1":2}; e2={"pid":"qd_P_xiangqing","eid":"","l1":2}; _yep_uuid=20b96334-a47a-a91f-90e4-9146574a95e5; _csrfToken=TncONJxjL6W4HdzI8lhARsXA8VLBv0pFZHk4vLGt; newstatisticUUID=1610784484_103881423; mrecUUID=8240008f0d801de3533e22506612a666; qdrs=0|3|0|0|1; qdgd=1; showSectionCommentGuide=1; lrbc=1025080261|638034845|0,1025795591|631449770|0,1014104227|450856481|0; rcr=1025080261,1025795591,1014104227; e1={"pid":"qd_P_Searchresult","eid":"qd_S05","l1":3}; e2={"pid":"qd_p_qidian","eid":"qd_H_Search","l1":2}'
    split_lists = cookie_str2.split(";")
    cookie_dict = {}
    for i in split_lists:
        i_split = i.split('=')
        cookie_dict[i_split[0].strip()] = i_split[1]
    print(split_lists, len(split_lists))
    print(cookie_dict)