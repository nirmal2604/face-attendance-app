import redis

r = redis.StrictRedis(
    host='redis-19281.c266.us-east-1-3.ec2.redns.redis-cloud.com',
    port=19281,
    decode_responses=True,  # get strings
    username="default",
    password="CrNlVSNyrJ9cRz4IeOTZSrnu5Yf55ynq",
)

print("Listing all fields in academy:register:")
fields = r.hkeys('academy:register')
for f in fields:
    print(f)
