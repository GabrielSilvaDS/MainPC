print('=' * 15, 'CONTAGEM PRO FIM DE ANO', '=' * 15)
from time import sleep
import emoji
for a in range(10, 0, -1):
    sleep(1)
    print(a)
sleep(1)
print('{} BOOOM!!! {}'.format(emoji.emojize(':fireworks:'), emoji.emojize(':fireworks:')))
