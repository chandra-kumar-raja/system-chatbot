import speedtest
from functools import lru_cache

@lru_cache(maxsize=1)
def get_network_info():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping

        return {
            "Download Speed (Mbps)": round(download_speed, 2),
            "Upload Speed (Mbps)": round(upload_speed, 2),
            "Ping (ms)": ping
        }
    except Exception as e:
        return {"Error": str(e)}
