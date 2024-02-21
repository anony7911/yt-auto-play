from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import random
from selenium.webdriver.common.keys import Keys

def create_webdriver():
    ua = UserAgent()
    
    chrome_options = Options()
    user_agent = ua.random
    chrome_options.add_argument(f'user-agent={user_agent}')
    
    # Aktifkan mode headless
    # chrome_options.add_argument('--headless')
    
    #ukuran browser full screen
    chrome_options.add_argument("--start-maximized")
    
    # Sesuaikan path dengan lokasi chromedriver di komputer Anda
    driver_path = 'D:\kecca\youtube\chromedriver.exe'
    
    # Buat instance WebDriver dengan opsi yang telah diatur
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    
    return driver, user_agent

def search_and_play(driver, search_query):
    try:
        # Ganti URL sesuai dengan halaman yang ingin Anda buka
        driver.get('https://www.youtube.com')

        # Tunggu beberapa detik untuk memastikan halaman sudah terbuka
        time.sleep(7)  # Sesuaikan dengan kebutuhan

        # Cari elemen kotak pencarian dan kirimkan query
        search_box = driver.find_element(By.NAME, 'search_query')
        search_box.send_keys(search_query)

        # Tekan Enter untuk melakukan pencarian
        search_box.send_keys(Keys.RETURN)

        # Tunggu beberapa detik untuk hasil pencarian muncul
        time.sleep(7)

        # Pilih video pertama dari hasil pencarian
        first_result = driver.find_element(By.CSS_SELECTOR, 'ytd-video-renderer')

        # Dapatkan judul video dari elemen first_result
        video_title_element = first_result.find_element(By.CSS_SELECTOR, '#title-wrapper')
        video_title_text = video_title_element.text

        # Klik pada video pertama
        first_result.click()

        # Cetak judul video yang dipilih
        print(f"Selected Video Title: {video_title_text}")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("An error occurred. Please check the configuration.")

def main(num_drivers):
    # Tambahkan beberapa variasi waktu untuk membuatnya lebih acak
    wait_time = random.randint(3, 10)
    print(f"Waiting for {wait_time} seconds before starting...")
    time.sleep(wait_time)

    # Inisialisasi list untuk menyimpan driver dan user agent
    drivers = []
    user_agents = []

    # Loop untuk membuat dan menjalankan driver sebanyak num_drivers
    for i in range(num_drivers):
        driver, user_agent = create_webdriver()
        drivers.append(driver)
        user_agents.append(user_agent)
        
        # Cetak user agent yang digunakan pada masing-masing driver
        print(f"Using User Agent for Driver {i+1}: {user_agent}")

        # List judul yang akan diacak
        judul_list = ["buat yang hobi mancing wajib nonton nih || karena mancing harus sabar !! jadi ya sabar aja", "Bukan mukbang, cuman makan biasa!!", "gerak jalan bebas part akhir||pawai kemerdekaan"]

        # Pilih judul secara acak
        random_judul = random.choice(judul_list)

        # Menjalankan fungsi pencarian dan pemutaran video dengan judul yang telah dipilih pada driver saat ini
        search_and_play(driver, random_judul)

        # Tahan selama 4-6 menit (240-360 detik, random)
        play_time = random.randint(240, 360)
        print(f"Playing for {play_time} seconds...")
        time.sleep(play_time)

    # Tutup semua browser setelah selesai memutar video
    for driver in drivers:
        driver.quit()

if __name__ == "__main__":
    # Masukkan jumlah driver yang diinginkan, misalnya 3
    main(3)
