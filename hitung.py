import streamlit as st

st.title("Kalkulator Pembagian")

# Input angka dari pengguna
angka_input = st.text_input("Masukkan angka:")
angka_bagi = st.text_input("Masukkan angka bagi :")
if angka_input:
    try:
        angka = int(angka_input)
        hasil = 10 / angka_bagi
        st.success(f"Hasil: {hasil:.2f}")
    except ZeroDivisionError:
        st.error("Angka tidak boleh nol.")
    except ValueError:
        st.error("Masukkan angka bulat yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan lain: {e}")
