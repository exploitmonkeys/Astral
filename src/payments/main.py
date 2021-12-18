import sql
from wrapper import PaymentAPI

private_key = ''
public_key = ''
txid = ''

API = PaymentAPI(
    transid = txid, 
    privkey = private_key, 
    pubkey = public_key
)

query = API.createRequest()

if query:
    connection = sql(host='localhost', port=3306)

    db = connection.listQuery(
        user = 'root',
        password = 'very_strong_password',
        database = 'database',
    )

    cursor = db.cursor()

    cursor.execute(f"INSERT INTO `verified_users` (`ipaddress`, `email`, `user`, `date`) VALUES ('{query['ipaddress']}', '{query['email']}', '{query['username']}', CURRENT_DATE());")
    db.commit()


