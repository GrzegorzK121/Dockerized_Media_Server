# 🚀 Dockerized Media Server 📡🎥  

### **Zaawansowana aplikacja webowa do zarządzania multimediami i kontenerami Docker**  

## 📌 **Opis projektu**  
**Dockerized Media Server** to konteneryzowana aplikacja webowa umożliwiająca **przesyłanie, przechowywanie i wyświetlanie multimediów** oraz **zarządzanie kontenerami Docker**. System działa w **zwirtualizowanym środowisku na VirtualBox z Debianem**, zapewniając **wysoką izolację procesów, automatyzację wdrożeń oraz monitoring zasobów serwera**.

---

## ⚙ **Technologie**
🔹 **Backend**: Flask + SQLite  
🔹 **Frontend**: HTML, CSS, JavaScript (Jinja2)  
🔹 **Konteneryzacja**: Docker, Docker Compose  
🔹 **Monitorowanie**: Prometheus, Grafana  
🔹 **Serwer**: VirtualBox + Debian  
🔹 **Open-Source** – projekt w pełni oparty na otwartym kodzie  

---

## 🎯 **Funkcjonalności**
✅ **Rejestracja i logowanie użytkowników** (z obsługą ról – admin/user)  
✅ **Zarządzanie plikami multimedialnymi** (upload, przechowywanie, podgląd)  
✅ **Dynamiczne menu** ładowane z osobnego pliku (`menu.html`)  
✅ **Panel administracyjny do zarządzania Dockerem** (start/stop kontenerów)  
✅ **Przechowywanie multimediów w kontenerze** (izolacja danych)  
✅ **Wykresy zużycia CPU, RAM oraz statystyk plików** (Prometheus + Grafana)  

---

## 🚀 **Uruchomienie projektu**  

**1️⃣ Klonowanie repozytorium:**  
```bash
git clone https://github.com/GrzegorzK121/Dockerized_Media_Server.git
cd Dockerized_Media_Server
