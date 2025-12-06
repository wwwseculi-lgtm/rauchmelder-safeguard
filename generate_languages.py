#!/usr/bin/env python3
"""
Multi-Language Website Generator
Creates translated versions of the Secu.li website
"""

import os

LANGUAGES = {
    "en": {
        "name": "English",
        "flag": "🇬🇧",
        "translations": {
            "title": "Secu.li | Smoke Detectors & Fire Safety for Europe",
            "meta_desc": "Secu.li - Your European partner for smoke detectors, CO detectors and professional fire safety solutions. EU-certified, 10-year battery, smart home compatible.",
            "nav_home": "Home",
            "nav_products": "Products",
            "nav_service": "Installation & Service",
            "nav_about": "About Us",
            "nav_contact": "Contact",
            "cta_button": "Get Quote",
            "hero_badge": "🏆 EU-Certified Fire Safety",
            "hero_title": "Professional Smoke Detector Service",
            "hero_subtitle": "Installation, maintenance and inspection of smoke detectors throughout Europe. Your safety is our priority.",
            "hero_cta1": "Free Consultation",
            "hero_cta2": "Call Now",
            "trust_ce": "CE Certified",
            "trust_tuv": "TÜV Tested",
            "trust_vds": "VdS Approved",
            "trust_10y": "10 Year Warranty",
            "section_service": "Service Area",
            "section_service_title": "Our Service in Europe",
            "section_service_desc": "Professional smoke detector installation and maintenance in these countries.",
            "available": "Available",
            "partial": "Partial",
            "de_desc": "Full coverage",
            "at_desc": "All provinces",
            "ch_desc": "Entire country",
            "contact_badge": "Get in Touch",
            "contact_title": "Request Free Consultation",
            "contact_subtitle": "Response within 24 hours - free and non-binding.",
            "form_name": "Name *",
            "form_email": "Email *",
            "form_phone": "Phone",
            "form_country": "Country *",
            "form_city": "City *",
            "form_subject": "Subject *",
            "form_message": "Your Message *",
            "form_submit": "Send Request →",
            "form_privacy": "🔒 Your data is secure.",
            "footer_rights": "All rights reserved.",
            "footer_imprint": "Imprint",
            "footer_privacy": "Privacy Policy",
        }
    },
    "sr": {
        "name": "Srpski",
        "flag": "🇷🇸",
        "translations": {
            "title": "Secu.li | Detektori Dima i Protivpožarna Zaštita za Evropu",
            "meta_desc": "Secu.li - Vaš evropski partner za detektore dima, CO detektore i profesionalna protivpožarna rešenja. EU sertifikat, 10 godina baterije.",
            "nav_home": "Početna",
            "nav_products": "Proizvodi",
            "nav_service": "Montaža i Servis",
            "nav_about": "O Nama",
            "nav_contact": "Kontakt",
            "cta_button": "Zatražite Ponudu",
            "hero_badge": "🏆 EU-Sertifikovana Protivpožarna Zaštita",
            "hero_title": "Profesionalni Servis za Detektore Dima",
            "hero_subtitle": "Instalacija, održavanje i inspekcija detektora dima širom Evrope. Vaša bezbednost je naš prioritet.",
            "hero_cta1": "Besplatna Konsultacija",
            "hero_cta2": "Pozovite Nas",
            "trust_ce": "CE Sertifikat",
            "trust_tuv": "TÜV Testiran",
            "trust_vds": "VdS Odobren",
            "trust_10y": "10 Godina Garancije",
            "section_service": "Područje Servisa",
            "section_service_title": "Naš Servis u Evropi",
            "section_service_desc": "Profesionalna instalacija i održavanje detektora dima u ovim zemljama.",
            "available": "Dostupno",
            "partial": "Delimično",
            "de_desc": "Puna pokrivenost",
            "at_desc": "Sve pokrajine",
            "ch_desc": "Cela zemlja",
            "contact_badge": "Kontaktirajte Nas",
            "contact_title": "Zatražite Besplatnu Konsultaciju",
            "contact_subtitle": "Odgovor u roku od 24 sata - besplatno i neobavezujuće.",
            "form_name": "Ime *",
            "form_email": "Email *",
            "form_phone": "Telefon",
            "form_country": "Država *",
            "form_city": "Grad *",
            "form_subject": "Tema *",
            "form_message": "Vaša Poruka *",
            "form_submit": "Pošaljite Zahtev →",
            "form_privacy": "🔒 Vaši podaci su sigurni.",
            "footer_rights": "Sva prava zadržana.",
            "footer_imprint": "Impresum",
            "footer_privacy": "Politika Privatnosti",
        }
    },
    "hr": {
        "name": "Hrvatski",
        "flag": "🇭🇷",
        "translations": {
            "title": "Secu.li | Detektori Dima i Protupožarna Zaštita za Europu",
            "meta_desc": "Secu.li - Vaš europski partner za detektore dima, CO detektore i profesionalna protupožarna rješenja. EU certifikat, 10 godina baterije.",
            "nav_home": "Početna",
            "nav_products": "Proizvodi",
            "nav_service": "Montaža i Servis",
            "nav_about": "O Nama",
            "nav_contact": "Kontakt",
            "cta_button": "Zatražite Ponudu",
            "hero_badge": "🏆 EU-Certificirana Protupožarna Zaštita",
            "hero_title": "Profesionalni Servis za Detektore Dima",
            "hero_subtitle": "Instalacija, održavanje i inspekcija detektora dima diljem Europe. Vaša sigurnost je naš prioritet.",
            "hero_cta1": "Besplatna Konzultacija",
            "hero_cta2": "Nazovite Nas",
            "trust_ce": "CE Certifikat",
            "trust_tuv": "TÜV Testiran",
            "trust_vds": "VdS Odobren",
            "trust_10y": "10 Godina Jamstva",
            "section_service": "Područje Servisa",
            "section_service_title": "Naš Servis u Europi",
            "section_service_desc": "Profesionalna instalacija i održavanje detektora dima u ovim zemljama.",
            "available": "Dostupno",
            "partial": "Djelomično",
            "de_desc": "Puna pokrivenost",
            "at_desc": "Sve pokrajine",
            "ch_desc": "Cijela zemlja",
            "contact_badge": "Kontaktirajte Nas",
            "contact_title": "Zatražite Besplatnu Konzultaciju",
            "contact_subtitle": "Odgovor u roku od 24 sata - besplatno i neobvezujuće.",
            "form_name": "Ime *",
            "form_email": "Email *",
            "form_phone": "Telefon",
            "form_country": "Država *",
            "form_city": "Grad *",
            "form_subject": "Tema *",
            "form_message": "Vaša Poruka *",
            "form_submit": "Pošaljite Zahtjev →",
            "form_privacy": "🔒 Vaši podaci su sigurni.",
            "footer_rights": "Sva prava pridržana.",
            "footer_imprint": "Impresum",
            "footer_privacy": "Politika Privatnosti",
        }
    },
    "bg": {
        "name": "Български",
        "flag": "🇧🇬",
        "translations": {
            "title": "Secu.li | Пожароизвестители и Противопожарна Защита за Европа",
            "meta_desc": "Secu.li - Вашият европейски партньор за пожароизвестители, CO детектори и професионални противопожарни решения. ЕС сертификат, 10 години батерия.",
            "nav_home": "Начало",
            "nav_products": "Продукти",
            "nav_service": "Монтаж и Сервиз",
            "nav_about": "За Нас",
            "nav_contact": "Контакт",
            "cta_button": "Заявете Оферта",
            "hero_badge": "🏆 ЕС-Сертифицирана Противопожарна Защита",
            "hero_title": "Професионален Сервиз за Пожароизвестители",
            "hero_subtitle": "Инсталация, поддръжка и проверка на пожароизвестители в цяла Европа. Вашата безопасност е наш приоритет.",
            "hero_cta1": "Безплатна Консултация",
            "hero_cta2": "Обадете се",
            "trust_ce": "CE Сертификат",
            "trust_tuv": "TÜV Тестван",
            "trust_vds": "VdS Одобрен",
            "trust_10y": "10 Години Гаранция",
            "section_service": "Зона на Обслужване",
            "section_service_title": "Нашият Сервиз в Европа",
            "section_service_desc": "Професионална инсталация и поддръжка на пожароизвестители в тези страни.",
            "available": "Наличен",
            "partial": "Частичен",
            "de_desc": "Пълно покритие",
            "at_desc": "Всички провинции",
            "ch_desc": "Цялата страна",
            "contact_badge": "Свържете се с нас",
            "contact_title": "Заявете Безплатна Консултация",
            "contact_subtitle": "Отговор до 24 часа - безплатно и необвързващо.",
            "form_name": "Име *",
            "form_email": "Имейл *",
            "form_phone": "Телефон",
            "form_country": "Държава *",
            "form_city": "Град *",
            "form_subject": "Тема *",
            "form_message": "Вашето Съобщение *",
            "form_submit": "Изпратете Заявка →",
            "form_privacy": "🔒 Вашите данни са защитени.",
            "footer_rights": "Всички права запазени.",
            "footer_imprint": "Импресум",
            "footer_privacy": "Политика за Поверителност",
        }
    },
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles.css">
    <link rel="manifest" href="../manifest.json">
    <meta name="theme-color" content="#005AA9">
    <link rel="apple-touch-icon" href="../icons/apple-touch-icon.png">
    <link rel="alternate" hreflang="de" href="https://secu.li/">
    <link rel="alternate" hreflang="en" href="https://secu.li/en/">
    <link rel="alternate" hreflang="sr" href="https://secu.li/sr/">
    <link rel="alternate" hreflang="hr" href="https://secu.li/hr/">
    <link rel="alternate" hreflang="bg" href="https://secu.li/bg/">
</head>
<body>
    <header class="header" id="header">
        <div class="container">
            <a href="index.html" class="logo"><span>Secu.li</span></a>
            <nav class="nav">
                <ul class="nav-links">
                    <li><a href="index.html">{nav_home}</a></li>
                    <li><a href="../produkte.html">{nav_products}</a></li>
                    <li><a href="../service.html">{nav_service}</a></li>
                    <li><a href="../ueber-uns.html">{nav_about}</a></li>
                    <li><a href="kontakt.html">{nav_contact}</a></li>
                </ul>
                <div class="lang-switcher">
                    <select onchange="window.location.href=this.value">
                        <option value="../index.html">🇩🇪 DE</option>
                        <option value="../en/index.html" {en_sel}>🇬🇧 EN</option>
                        <option value="../sr/index.html" {sr_sel}>🇷🇸 SR</option>
                        <option value="../hr/index.html" {hr_sel}>🇭🇷 HR</option>
                        <option value="../bg/index.html" {bg_sel}>🇧🇬 BG</option>
                    </select>
                </div>
                <a href="kontakt.html" class="btn btn-primary">{cta_button}</a>
            </nav>
        </div>
    </header>

    <section class="hero hero-simple">
        <div class="container">
            <div class="hero-content hero-centered">
                <div class="hero-text">
                    <span class="hero-badge-top">{hero_badge}</span>
                    <h1>{hero_title}</h1>
                    <p class="subtitle">{hero_subtitle}</p>
                    <div class="hero-buttons">
                        <a href="kontakt.html" class="btn btn-primary btn-lg">{hero_cta1}</a>
                        <a href="tel:+498001234567" class="btn btn-outline btn-lg">📞 {hero_cta2}</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="trust-badges-section">
        <div class="container">
            <div class="trust-badges-grid">
                <div class="trust-badge-item"><div class="badge-icon">CE</div><span>{trust_ce}</span></div>
                <div class="trust-badge-item"><div class="badge-icon">TÜV</div><span>{trust_tuv}</span></div>
                <div class="trust-badge-item"><div class="badge-icon">VdS</div><span>{trust_vds}</span></div>
                <div class="trust-badge-item"><div class="badge-icon">10J</div><span>{trust_10y}</span></div>
            </div>
        </div>
    </section>

    <section class="section bg-gray">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">{section_service}</span>
                <h2>{section_service_title}</h2>
                <p>{section_service_desc}</p>
            </div>
            <div class="countries-grid">
                <div class="country-card"><div class="country-flag">🇩🇪</div><h5>Deutschland</h5><p>{de_desc}</p><span class="country-status status-required">{available}</span></div>
                <div class="country-card"><div class="country-flag">🇦🇹</div><h5>Österreich</h5><p>{at_desc}</p><span class="country-status status-required">{available}</span></div>
                <div class="country-card"><div class="country-flag">🇨🇭</div><h5>Schweiz</h5><p>{ch_desc}</p><span class="country-status status-required">{available}</span></div>
                <div class="country-card"><div class="country-flag">🇵🇱</div><h5>Polska</h5><p>{de_desc}</p><span class="country-status status-required">{available}</span></div>
                <div class="country-card"><div class="country-flag">🇧🇬</div><h5>България</h5><p>{de_desc}</p><span class="country-status status-required">{available}</span></div>
                <div class="country-card"><div class="country-flag">🇷🇸</div><h5>Srbija</h5><p>{de_desc}</p><span class="country-status status-required">{available}</span></div>
                <div class="country-card"><div class="country-flag">🇭🇷</div><h5>Hrvatska</h5><p>{de_desc}</p><span class="country-status status-required">{available}</span></div>
            </div>
        </div>
    </section>

    <section class="contact-form-section" id="kontaktformular">
        <div class="container">
            <div class="contact-header-centered">
                <span class="section-badge">{contact_badge}</span>
                <h2>{contact_title}</h2>
                <p>{contact_subtitle}</p>
            </div>
            <div class="contact-form-card contact-form-large">
                <form class="contact-form" id="contactForm">
                    <div class="form-grid-3">
                        <div class="form-group"><label for="name">{form_name}</label><input type="text" id="name" name="name" required></div>
                        <div class="form-group"><label for="email">{form_email}</label><input type="email" id="email" name="email" required></div>
                        <div class="form-group"><label for="phone">{form_phone}</label><input type="tel" id="phone" name="phone"></div>
                    </div>
                    <div class="form-grid-2">
                        <div class="form-group"><label for="country">{form_country}</label><input type="text" id="country" name="country" required></div>
                        <div class="form-group"><label for="city">{form_city}</label><input type="text" id="city" name="city" required></div>
                    </div>
                    <div class="form-group"><label for="message">{form_message}</label><textarea id="message" name="message" rows="4" required></textarea></div>
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary btn-xl">{form_submit}</button>
                        <p class="form-privacy">{form_privacy}</p>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>© 2024 Secu.li. {footer_rights} | <a href="../impressum.html">{footer_imprint}</a> | <a href="../datenschutz.html">{footer_privacy}</a></p>
            </div>
        </div>
    </footer>
    <script src="../script.js"></script>
</body>
</html>'''

def generate_pages():
    for lang_code, lang_data in LANGUAGES.items():
        os.makedirs(lang_code, exist_ok=True)
        
        t = lang_data["translations"]
        
        # Selection markers
        selections = {f"{l}_sel": "selected" if l == lang_code else "" for l in LANGUAGES.keys()}
        
        content = TEMPLATE.format(
            lang_code=lang_code,
            **t,
            **selections
        )
        
        filepath = f"{lang_code}/index.html"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ {lang_data['flag']} {lang_data['name']} - {filepath}")
    
    print(f"\n🎉 {len(LANGUAGES)} Sprachversionen erstellt!")

if __name__ == "__main__":
    generate_pages()
