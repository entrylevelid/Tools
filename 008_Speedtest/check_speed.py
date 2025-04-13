# =============================================
#  Entry Level ID
# =============================================

import speedtest as st

def speed_test():
    test = st.Speedtest()

    print("Starting speed test...")
    print("Testing download speed, please wait...")
    downspeed = test.download()
    downspeed = round(downspeed / 10**6, 2)
    print(f"Download speed : {downspeed} Mbps")

    print("Testing upload speed, please wait...")
    upspeed = test.upload()
    upspeed = round(upspeed / 10**6, 2)
    print(f"Upload speed : {upspeed} Mbps")

    print("Measuring ping...")
    ping = test.results.ping
    print("Ping : ", ping)

speed_test()