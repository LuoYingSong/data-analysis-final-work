import requests
import os

main_path = 'preprocess_data_trans'
code_list = ['0900952', '0900945', '0900914', '0900903', '0603967', '0603885', '0603871', '0603813', '0603713', '0603535', '0603329', '0603223', '0603167', '0603128', '0603069', '0603066', '0603056', '0603032', '0601975', '0601919', '0601880', '0601872', '0601866', '0601598', '0601518', '0601333', '0601326', '0601298', '0601228', '0601188', '0601111', '0601107', '0601021', '0601018', '0601008', '0601006', '0601000', '0600897', '0600834', '0600798', '0600794', '0600787', '0600717', '0600676', '0600662', '0600650', '0600611', '0600575', '0600561', '0600548', '0600428', '0600377', '0600368', '0600350', '0600317', '0600279', '0600270', '0600269', '0600233', '0600221', '0600190', '0600179', '0600125', '0600119', '0600115', '0600106', '0600035', '0600033', '0600029', '0600026', '0600020', '0600018', '0600017', '0600012', '0600009', '0600004', '1300240', '1300013', '1201872', '1200429', '1200152', '1200022', '1002930', '1002928', '1002800', '1002711', '1002682', '1002627', '1002492', '1002468', '1002357', '1002352', '1002320', '1002245', '1002120', '1002040', '1001965', '1001872', '1000905', '1000900', '1000885', '1000828', '1000755', '1000582', '1000557', '1000548', '1000520', '1000507', '1000429', '1000099', '1000089', '1000088', '1000022']

for code in code_list:
    code = code[1:]
    if not os.path.exists(main_path+'/{}'.format(code)):
        os.mkdir(main_path+'/{}'.format(code))
    file_type = ['', 'ylnl', 'chnl', 'cznl', 'yynl']
    for type_ in file_type:
        if type_ == '':
            url = 'http://quotes.money.163.com/service/zycwzb_{}.html?type=report'.format(code)
            type_ = 'main'
        else:
            url = 'http://quotes.money.163.com/service/zycwzb_{}.html?type=report&part={}'.format(code, type_)
        file = requests.get(url)
        with open(main_path+'/{}/{}.csv'.format(code, type_), 'w') as f:
            f.write(file.content.decode('gbk'))
