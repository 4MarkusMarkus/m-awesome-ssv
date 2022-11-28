from web3 import Web3

web_th = Web3(Web3.HTTPProvider("http://localhost:8545"))
abi = [{
    "inputs": [
        {
            "internalType": "bytes",
            "name": "publicKey",
            "type": "bytes"
        },
        {
            "internalType": "uint32[]",
            "name": "operatorIds",
            "type": "uint32[]"
        },
        {
            "internalType": "bytes[]",
            "name": "sharesPublicKeys",
            "type": "bytes[]"
        },
        {
            "internalType": "bytes[]",
            "name": "sharesEncrypted",
            "type": "bytes[]"
        },
        {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
        }
    ],
    "name": "registerValidator",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
}]
# print(web_th.eth.get_balance("0x2279B7A0a67DB372996a5FaB50D91eAA73d2eBe6"))
# exit()
account = web_th.eth.account.privateKeyToAccount("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
abi_token_ssv = [{
    "inputs": [
        {
            "internalType": "address",
            "name": "to",
            "type": "address"
        },
        {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
        }
    ],
    "name": "transfer",
    "outputs": [
        {
            "internalType": "bool",
            "name": "",
            "type": "bool"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
}, {
    "inputs": [
        {
            "internalType": "address",
            "name": "spender",
            "type": "address"
        },
        {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
        }
    ],
    "name": "approve",
    "outputs": [
        {
            "internalType": "bool",
            "name": "",
            "type": "bool"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
}]
# ssv = web_th.eth.contract(abi=abi_token_ssv, address="0x0165878A594ca255338adfa4d48449f69242Eb8F")
# tx = ssv.functions.transfer("0xc351628EB244ec633d5f21fBD6621e1a683B1181",100000000000000000000).buildTransaction()
pool = web_th.eth.contract(abi=abi, address=Web3.toChecksumAddress("0xA51c1fc2f0D1a1b8494Ed1FE312d7C3a78Ed91C0"))

token = web_th.eth.contract(abi=abi_token_ssv, address=Web3.toChecksumAddress("0x610178dA211FEF7D417bC0e6FeD39F05609AD788"))
# print(token.functions.balanceOf(account.address).call())
tx_app = token.functions.approve("0xA51c1fc2f0D1a1b8494Ed1FE312d7C3a78Ed91C0",29725951960000000000).buildTransaction(
    {'from': account.address, 'gasPrice': web_th.toWei('2', 'gwei'), 'gas': 5000000})
tx_app['nonce'] = web_th.eth.get_transaction_count(account.address)
signed_tx = web_th.eth.account.sign_transaction(tx_app, account.key)
tx_hash = web_th.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = web_th.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)
if tx_receipt.status == 1:
    print('TX successful')
else:
    print('TX reverted')
tx = pool.functions.registerValidator(
    '0x96b22966c504b6a7ad41ee4f1fcc69c1f3293c3e4c70f4acdbebc1fc69db8d436aae24c5ad0a2b650475d69c061b0473',
    [1, 2, 9, 42],
    ['0xa3fd8193fedcfc0a6a9c719238461bc05584b22615a6592d373c4173e039a65db0a4ce5d251ed955c8e6c9c739ad989d',
     '0xa1bce6ee8d759c74b1ee924a84f277fb2784cb0b920fb52d0ba5097c6528f27a3c60ab3e25c3a93c36fe90e5fa9b07c0',
     '0xa491ea24bfa3fd2430293cfbac24a526d315702f7a686ce9cb6bfbc31479ba591b32fbe29be0cdd568fc22687ee0d0fb',
     '0x81a0a649733603687bb02b1bc300e6a1f4042b1f6a9834a0b2eae073f98ae09150fc3fed1e8373410ecc6872a5180088'],
    ['0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000001584933662f4865426776324d4b6e73764d504f43496c48495537765779384a516c793534507a3979695879365a305233434f676556754f53306f36674544307445486b347074626a44394c584330483074356a4e7873415a795645554e444b637556723045314e51625a375035373169594135686f693665324e2b585a454664417268354e49306b442f6a5749545164686e526850694e643435467151644845664f706c527a69446e786e5768424f533951586944356a624438545769654931317975736c6f5a66563946333462346f43667a50673843375331684b464c6d396777622f676543562b712f48364f57474b787947716338485269664537636673335570524e5132496d4561706e2f4b46326e6838617454464d6e4d7a794b744c3345714d4e6550375479716242663065524e2f3844524370363036756763434f6d32506d2b7054655a68423466674b78332f50592b66673d3d0000000000000000',
    '0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000001585a335a7933506c53536e464c4464774c2f6b5a6d483877715679474f4963463179494a626e634a47557a446f504b50514b554651313275675752312b347474312f645a53335768323565785070487730545a755049686335686a786352474e385541776e6135744a675332384f5771444f794f4c4d434254496f4e397231434f53664a3038726338522f6b615047677650714f4e6f7136613033316664387a7847674146494648735261615a67495848466b3255614f725955335562432b5a3148436c6a4a54784a7978624d32394d775134753567753473744e315049307148417a587730715139647a5a6d76515462436c58635854644e476c6e51694c41425963697435494f7064547a6d536f30734d6f336b5964517676567a4a376c767334704551736462766143595653374c7a35753061524f596f466e6342312f656d33436a7277446c30416343725a4f6c766176534878773d3d0000000000000000',
    '0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000001585a2f6358476e4549655535706b7652664e796278334b715a3152616551314e74504d447047557061655374487a5175424745525261586f6c5739302b63625541646f6a455674595770764f68776f7346634e725451695a7348357253796578754d322b467450756a75624c5432656862416c5976764d616a65424779394a4a4d674f2f4d53624a54324f586564683071716963512f5a56555764436d2f717a627677682f5575694d703135776762623439612b6567497867636572616c4763744433656d5550375543304d5338315269716f614b4e4c334557726233306853625730546964713149703739483451713072346d474e7631764b7636474a67724c63306548323136636f7452373258617a5a6731374d786c453430345865796b6276427075387864346f6b2b526135654f397a39642f416c592f4c69464e4b6f4548364b4f6d494c344b4661564e647a316a67305943413d3d0000000000000000',
    '0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000001587077303862536e5a6369422f62766d72704f2f3551327655686574337571752b637145656b4332376d2f31674b6c334743316771637039554a4b7a75544934724d436c3050654d7651725072414a32576139754f4679366b31796f654c47676143516c53514675643161546471727241476831502b786c4475337770486e50366b50787248785275534956662b69795748444c4b697065675934367a35786b386c4d48324b4b4c7634744a49704165354f33786b4d6974764248732b6b716e616d7632544374636e795767324a6b57713051466e764e354535386933692b7435424c46316b584e2b4e6a48447a396d6c49787070437969592b5a6845395a67556330745a514a454b664937737771717a5a4758724d74496233324f4475644f386936594e484a414f4a6b3733365865654c4c6956447149434a6d737a6b554547776d526933786e65516c4d2f645339695065595246513d3d0000000000000000'],
    19725951960000000000
).buildTransaction(
    {'from': account.address, 'gasPrice': web_th.toWei('2', 'gwei'), 'gas': 5000000})
tx['nonce'] = web_th.eth.get_transaction_count(account.address)
signed_tx = web_th.eth.account.sign_transaction(tx, account.key)
tx_hash = web_th.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = web_th.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)
if tx_receipt.status == 1:
    print('TX successful')
else:
    print('TX reverted')



