# Skrip Otomatisasi YouTube

Skrip Python ini mengotomatisasi pencarian dan pemutaran video YouTube menggunakan Selenium.

## Prasyarat

Sebelum menjalankan skrip, pastikan Anda telah menginstal hal-hal berikut:

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Chrome Browser](https://www.google.com/chrome/)

## Instalasi

1. Klona repositori ke komputer lokal Anda:

    ```bash
    git clone https://github.com/anony7911/yt-auto-play.git
    ```

2. Buka direktori proyek:

    ```bash
    cd yt-auto-play
    ```

3. Buat lingkungan virtual (opsional tetapi disarankan):

    ```bash
    python -m venv venv
    ```

4. Aktifkan lingkungan virtual:

    - Pada Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - Pada macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Instal paket yang diperlukan:

    ```bash
    pip install -r requirements.txt
    ```

6. Unduh [ChromeDriver](https://sites.google.com/chromium.org/driver/) dan letakkan di direktori proyek.

## Penggunaan

1. Buka file `yt.py` di editor teks.

2. Perbarui variabel `driver_path` dengan path yang benar ke eksekutor ChromeDriver.

    ```python
    driver_path = 'path/to/chromedriver.exe'
    ```

3. Jalankan skrip:

    ```bash
    python yt.py
    ```

Gantilah `yt.py` dengan nama sebenarnya dari skrip Python Anda.

## Catatan

- Skrip menggunakan agen pengguna acak untuk setiap instansi WebDriver untuk meniru perangkat yang berbeda. Jika diperlukan, Anda dapat memodifikasi fungsi `create_webdriver` untuk menggunakan agen pengguna tertentu.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
