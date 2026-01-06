import streamlit as st

st.title("Kalkulator Pembagian")

# Input angka dari pengguna
angka_input = int(st.text_input("Masukkan angka:"))
angka_bagi = int(st.text_input("Masukkan angka bagi :"))
if angka_input:
    try:
        hasil = angka_input / angka_bagi
        st.success(f"Hasil: {hasil:.2f}")
    except ZeroDivisionError:
        st.error("Angka tidak boleh nol.")
    except ValueError:
        st.error("Masukkan angka bulat yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan lain: {e}")
