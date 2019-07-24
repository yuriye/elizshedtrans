import converter.mytime as mytime


class Day:

    def __init__(self, eliz_fromto='', eliz_len='', isVillage = False):  # Конструктор
        self.__set_fields(eliz_fromto, eliz_len, isVillage)

    def __set_fields(self, eliz_fromto='', eliz_len='', isVillage = False):
        self.code = ''
        self.start = ''
        self.fin = ''
        self.len = ''
        self.pause = 60 if isVillage else 45

        if eliz_fromto is None:
            return
        if eliz_fromto == '' and eliz_len == '':
            return

        parts_len = eliz_len.__str__().split(':')
        if len(parts_len) == 1:
            parts_len.append('')
        self.len = parts_len[0] + ':' + parts_len[1]


        tmp = eliz_fromto.split('/')
        eliz_fromto = eliz_fromto.split('/')[0]
        parts_fromto = eliz_fromto.split('-')

        if len(parts_fromto) == 1:
            self.code = {
                parts_fromto[0] == 'О': 'ОТ',
                parts_fromto[0] == 'В': 'В',
                parts_fromto[0] == 'Б': 'Б'
            }.get(True)
            if self.code != None:
                return

        self.code = 'Я'
        if len(tmp) > 1:
            parts_fromto[0] = tmp[1]
        if parts_fromto[0].strip() in {'ВУЛ', 'ПАР', 'ТЕР', 'ПИО', 'ЛЕС', 'КОР', 'СОК', 'НИК', 'РАЗ', 'НАГ', 'ЕЛ', }:
            self.pause = 60

            # if self.len == '8:00' or self.len == '08:00':
            #     self.fin = '18:00'
            # elif self.len == '7:00' or self.len == '07:00':
            #     self.fin = '17:00'
            # elif self.len == '7:12' or self.len == '07:12':
            #     self.fin = '17:12'
            # elif self.len == '6:12' or self.len == '06:12':
            #     self.fin = '16:12'
            # elif self.len == '4:00' or self.len == '04:00':
            #     self.pause = 0
            #     self.start = '10:00'
            #     self.fin = '14:00'
            # elif self.len == '4:48' or self.len == '04:48':
            #     self.pause = 0
            #     self.start = '10:00'
            #     self.fin = '14:48'

            self.start = '9:00'
            if self.len == '4:00' or self.len == '04:00':
                self.pause = 0
                self.start = '10:00'
            elif self.len == '4:48' or self.len == '04:48':
                self.pause = 0
                self.start = '10:00'

            self.fin = self.__calculateFin()

            return

        parts_fromto = [str(parts_fromto[0]).strip() if len(parts_fromto) >= 1 else '',
                        str(parts_fromto[1]).strip() if len(parts_fromto) >= 2 else '']
        self.start = self.__dotstring_to_timestring(parts_fromto[0])
        # self.fin = self.__dotstring_to_timestring(parts_fromto[1])

        self.fin = self.__calculateFin()

    @staticmethod
    def __dotstring_to_timestring(in_str):
        if in_str == '' or in_str is None:
            return '00:00'

        parts = in_str.split('.')
        if len(parts) == 1:
            return parts[0] + ':00'
        parts[1] = parts[1][0:2]
        if len(parts[1]) == 1:
            parts[1] = parts[1] + '0'
        return parts[0] + ':' + parts[1]

    def get_len_in_minutes(self):
        try:
            parts = self.len.split(':')
            return int(parts[0]) * 60 + int(parts[1])
        except Exception:
            return 0

    def __calculateFin(self):
        if self.get_len_in_minutes() / 60 <= 5:
            self.pause = 0
        return str((mytime.MyTime(reprStr=self.start) +
             mytime.MyTime(minutes=str(self.pause))) +
            mytime.MyTime(reprStr=self.len))
