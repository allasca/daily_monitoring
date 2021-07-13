# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: /home/allasca/buildozer/.buildozer/android/app/main.py
# Compiled at: 2020-06-10 15:51:30
# Size of source mod 2**32: 10647 bytes
import webbrowser
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
import utils, json, urllib
from kivy.core.window import Window
from bs4 import BeautifulSoup
from kivy.clock import Clock
Window.softinput_mode = 'below_target'

class MainApp(MDApp):
    utils = utils

    def __init__(self, **kwargs):
        (super().__init__)(**kwargs)

    def on_start(self):
        global cfg
        with open('config.json', 'r', encoding='utf-8') as (con):
            a = con.read()
            cfg = json.loads(a)
            con.close()
        Clock.schedule_once(self.load_cfg, 2)

    def kirim_web(self):
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSeR2MToyyJGSIlgIOwhclBwxh1-WizX0pXuPaCFXXrRWBfTIA/formResponse?'
        body = urllib.parse.urlencode(cfg['form'])
        uri = url + body
        webbrowser.open(uri)

    def kirim_form(self):
        try:
            url = 'https://docs.google.com/forms/d/e/1FAIpQLSeR2MToyyJGSIlgIOwhclBwxh1-WizX0pXuPaCFXXrRWBfTIA/formResponse?'
            body = urllib.parse.urlencode(cfg['form'])
            uri = url + body
            self.res = UrlRequest(uri, method='POST', on_success=(self.kirim_sukses),
              on_error=(self.kirim_eror),
              on_failure=(self.kirim_fail),
              on_redirect=(self.kirim_redir))
        except Exception as err:
            try:
                self.root.ids.tab_dash.ids.kirim_log.text += '\n[b][color=#ff0000]{}[/color][/b]'.format(err)
            finally:
                err = None
                del err

    def kirim_sukses(self, r, res):
        self.root.ids.tab_dash.ids.kirim_log.text += '[b][color=#008000]\nFORM SUDAH TERKIRIM[/color][/b]'
        dat = '\n                </script></head><body dir="ltr" itemscope itemtype="http://schema.org/CreativeWork/FormObject" class="freebirdLightBackground " data-is-prepopulate-mode="false"><meta itemprop="name" content="test"><meta itemprop="description" content="test 123"><meta itemprop="faviconUrl" content="https://ssl.gstatic.com/docs/spreadsheets/forms/favicon_qp2.png"><meta itemprop="url" content="https://docs.google.com/forms/d/e/1FAIpQLSeDAIm9OvHmUzic7wYMJVo2CjHpq2dhWAASRqylM4VUzFPd-w/viewform?usp=embed_googleplus"><meta itemprop="embedURL" content="https://docs.google.com/forms/d/e/1FAIpQLSeDAIm9OvHmUzic7wYMJVo2CjHpq2dhWAASRqylM4VUzFPd-w/viewform?embedded=true&amp;usp=embed_googleplus"><meta itemprop="thumbnailUrl" content="https://ssl.gstatic.com/docs/forms/social/social-forms-big-2.png"><meta itemprop="image" content="https://ssl.gstatic.com/docs/forms/social/social-forms-big-2.png"><meta itemprop="imageUrl" content="https://ssl.gstatic.com/docs/forms/social/social-forms-big-2.png"><div class="freebirdFormviewerViewFormContentWrapper"><div class="freebirdFormviewerViewHeaderCard freebirdFormviewerViewCenteredContent freebirdViewerHeaderCard freebirdHeaderCard"></div><div class="freebirdFormviewerViewCenteredContent"><div class="freebirdFormviewerViewFormCard exportFormCard"><div class="freebirdFormviewerViewResponseConfirmContentContainer"><div class="freebirdFormviewerViewResponseThemeStripe freebirdSolidBackground"></div><div class="freebirdFormviewerViewResponsePageTitle freebirdCustomFont" role="heading" aria-level="1">test</div><div class="freebirdFormviewerViewResponseConfirmationMessage">Tanggapan Anda telah direkam.</div><div class="freebirdFormviewerViewResponseLinksContainer"><a href="https://docs.google.com/forms/d/e/1FAIpQLSeDAIm9OvHmUzic7wYMJVo2CjHpq2dhWAASRqylM4VUzFPd-w/viewform?usp=form_confirm">Kirim tanggapan lain</a></div></div></div><div><div class="freebirdFormviewerViewFooterDisclaimer freebirdDisclaimerColor">Konten ini tidak dibuat atau didukung oleh Google. <a href="reportabuse" target="_blank">Laporkan Penyalahgunaan</a> - <a href="https://policies.google.com/terms" target="_blank">Persyaratan Layanan</a> - <a href="https://policies.google.com/privacy" target="_blank">Kebijakan Privasi</a></div><div class="freebirdFormviewerViewFooterImageContainer freebirdFormviewerViewFooterPageBreak"><a dir="auto" href="//www.google.com/forms/about/?utm_source=product&utm_medium=forms_logo&utm_campaign=forms"><img src="https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_dark_clr_74x24px.svg" alt="Google" height="24px" width="74px"/>&nbsp;<span class="freebirdCommonViewProductnameLockupText">Formulir</span></a></div></div></div></div><div jscontroller="rK97wb" jsaction="rcuQ6b:HYsj2"></div><script id="base-js" src="https://www.gstatic.com/_/freebird/_/js/k=freebird.v.id.Tp9Ng5pbxP8.O/d=1/ct=zgms/rs=AMjVe6hJIboEtlMfpJ12K0R-52q8jEAJoQ/m=viewer_base" nonce="KBpwrlOZOh/nqhwiwxSOTA"></script></body></html>\n                '
        self.root.ids.tab_dash.ids.kirim_log.text += '\n' + dat

    def kirim_eror(self, r, res):
        self.root.ids.tab_dash.ids.kirim_log.text += '[b][color=#ff0000]\nPENGIRIMAN FORM ERROR[/color][/b]'

    def kirim_fail(self, r, res):
        self.root.ids.tab_dash.ids.kirim_log.text += '[b][color=#ff0000]\nError code = {}[/color][/b]'.format(r.resp_status)
        self.root.ids.tab_dash.ids.kirim_log.text += '[b][color=#ff0000]\nPENGIRIMAN FORM GAGAL[/color][/b]'

    def kirim_redir(self, r, res):
        self.root.ids.tab_dash.ids.kirim_log.text += '[b][color=#ff0000]\nFORM MASIH DITUTUP[/color][/b]'
        self.root.ids.tab_dash.ids.kirim_log.text += '\n' + res

    def load_cfg(self, *args):
        form = self.root.ids.tab_form.ids
        form.nama_lengkap.text = cfg['form']['entry.350118970']
        form.NPK.text = cfg['form']['entry.1074549873']
        form.satuan_unit.text = cfg['form']['entry.1774840932']
        form.jenjang_jabatan.text = cfg['form']['entry.1018645289']
        form.jabatan.text = cfg['form']['entry.584789158']
        form.karakteristik_jabatan.text = cfg['form']['entry.47690330']
        form.tugas_di.text = cfg['form']['entry.520473575']
        form.kondisi_kesehatan.text = cfg['form']['entry.947734472']
        form.kondisi_kesehatan_keluarga.text = cfg['form']['entry.516669719']
        form.lingkungan_ditetapkan.text = cfg['form']['entry.2081842325']
        form.protokol_pencegahan.text = cfg['form']['entry.1271880']
        form.protokol_yang_belum.text = cfg['form']['entry.108551673']
        form.absen_dani.text = cfg['form']['entry.1765189046']
        form.tugas_atasan.text = cfg['form']['entry.1687018518']
        form.tanya_tugas.text = cfg['form']['entry.637243096']
        form.target_penyelesaian.text = cfg['form']['entry.1753181683']
        form.menyelesaikan_target.text = cfg['form']['entry.1091811440']
        form.atasan_memonitor.text = cfg['form']['entry.238037399']
        form.atasan_arahan.text = cfg['form']['entry.1860507276']
        form.target_dicapai.text = cfg['form']['entry.1468725842']
        form.sosialisasi_budaya.text = cfg['form']['entry.772237847']
        form.perasaan.text = cfg['form']['entry.981737776']
        form.wfh_rencana.text = cfg['form']['entry.716350225']
        form.cara_protokol.text = cfg['form']['entry.124137136']
        datalist = cfg['form']['entry.1125313690']
        nama = form.list_list.children[0].text
        nilai = form.list_list.children[0].ids._right_container.children[0].active
        for y in range(7):
            if form.list_list.children[y].text in datalist:
                form.list_list.children[y].ids._right_container.children[0].active = True

    def save_cfg(self):
        form = self.root.ids.tab_form.ids
        cfg['form']['entry.350118970'] = form.nama_lengkap.text
        cfg['form']['entry.1074549873'] = form.NPK.text
        cfg['form']['entry.1774840932'] = form.satuan_unit.text
        cfg['form']['entry.1018645289'] = form.jenjang_jabatan.text
        cfg['form']['entry.584789158'] = form.jabatan.text
        cfg['form']['entry.47690330'] = form.karakteristik_jabatan.text
        cfg['form']['entry.520473575'] = form.tugas_di.text
        cfg['form']['entry.947734472'] = form.kondisi_kesehatan.text
        cfg['form']['entry.516669719'] = form.kondisi_kesehatan_keluarga.text
        cfg['form']['entry.2081842325'] = form.lingkungan_ditetapkan.text
        cfg['form']['entry.1271880'] = form.protokol_pencegahan.text
        cfg['form']['entry.108551673'] = form.protokol_yang_belum.text
        cfg['form']['entry.1765189046'] = form.absen_dani.text
        cfg['form']['entry.1687018518'] = form.tugas_atasan.text
        cfg['form']['entry.637243096'] = form.tanya_tugas.text
        cfg['form']['entry.1753181683'] = form.target_penyelesaian.text
        cfg['form']['entry.1091811440'] = form.menyelesaikan_target.text
        cfg['form']['entry.238037399'] = form.atasan_memonitor.text
        cfg['form']['entry.1860507276'] = form.atasan_arahan.text
        cfg['form']['entry.1468725842'] = form.target_dicapai.text
        cfg['form']['entry.772237847'] = form.sosialisasi_budaya.text
        cfg['form']['entry.981737776'] = form.perasaan.text
        cfg['form']['entry.716350225'] = form.wfh_rencana.text
        cfg['form']['entry.124137136'] = form.cara_protokol.text
        with open('config.json', 'w', encoding='utf-8') as (con):
            json.dump(cfg, con, ensure_ascii=False, indent='\t')
            con.flush()
            con.close()

    def auto_upper(self, target):
        target.text = target.text.upper()

    def cek_status_form(self):
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSeR2MToyyJGSIlgIOwhclBwxh1-WizX0pXuPaCFXXrRWBfTIA/viewform'
        self.req = UrlRequest(url, req_headers=(cfg['headers']), on_success=(self.cek_status_form_success), on_redirect=(self.cek_status_form_redirect))

    def cek_status_form_success(self, r, res):
        self.root.ids.tab_dash.ids.status.text = 'Form telah dibuka'
        self.root.ids.tab_dash.ids.status.theme_text_color = 'Custom'
        self.root.ids.tab_dash.ids.status.text_color = (0, 1, 0, 1)
        soup = BeautifulSoup(res, 'html.parser')
        head = soup.find_all('div', attrs={'class': 'freebirdFormviewerViewHeaderTitle exportFormTitle freebirdCustomFont'})[0].get_text().strip()
        self.root.ids.tab_dash.ids.judul.text = head

    def cek_status_form_redirect(self, r, res):
        if '<H1>Moved Temporarily</H1>' in res:
            self.root.ids.tab_dash.ids.status.text = 'Form ditutup'
            self.root.ids.tab_dash.ids.status.theme_text_color = 'Error'

    def list_tersedia(self, data, nama):
        list = cfg['form']['entry.1125313690']
        if data.active == True:
            if nama not in list:
                list.append(nama)
        if data.active == False:
            list.remove(nama)


if __name__ == '__main__':
    MainApp().run()