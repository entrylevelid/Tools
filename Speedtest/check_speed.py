import speedtest as st

def speed_test():
    test = st.Speedtest()

    downspeed = test.download()
    downspeed = round(downspeed / 10**6, 2)
    print(f"Download speed : {downspeed} Mbps")

    upspeed = test.upload()
    upspeed = round(upspeed / 10**6, 2)
    print(f"Upload speed : {upspeed} Mbps")

    ping = test.results.ping
    print("Ping : ", ping)

speed_test()
