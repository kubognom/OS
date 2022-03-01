import string
import hashlib
from _ast import In
import itertools
import multiprocessing
from functools import partial
import binascii
from datetime import datetime

hsh = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad', '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b', '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'


def brute_force1(mask, hsh, alphabet=string.ascii_letters + string.digits, verbose=False):
    pwd_pat = mask.replace('{', '{{').replace('}', '}}').replace('*', '{}')
    N = mask.count('*')
    i = 0
    for chars in itertools.product(alphabet, repeat=N):
        if verbose:
            i += 1
            if i % 10000 == 0:
                print('Итераций >>> {}'.format(i))
        if hsh == hashlib.sha256(pwd_pat.format(*chars).encode()).hexdigest():
            print('паролль = ', pwd_pat.format(*chars))
            return pwd_pat.format(*chars)
    return None





alphabet = string.ascii_lowercase.encode()


def sha256(data):
    return hashlib.sha256(data).digest()


def check_sha256(repls_parent, bytes_format, n, target_sha256):
    for repls in itertools.product(alphabet, repeat=n):
        data = bytes_format % (repls_parent + repls)
        if sha256(data) == target_sha256:
            return data


def brute_force2(mask, target_sha256, n_cutoff=4):
    bytes_format = mask.replace(b'%', b'%%').replace(b'*', b'%c')
    mp_check = partial(check_sha256,
                       bytes_format=bytes_format,
                       n=min(n_cutoff, mask.count(b'*')),
                       target_sha256=target_sha256)
    n = max(0, mask.count(b'*') - n_cutoff)
    all_repls_parent = itertools.product(alphabet, repeat=n)
    with multiprocessing.Pool() as pool:
        for data in pool.imap_unordered(mp_check, all_repls_parent):
            if data is not None:
                return data

if __name__ == '__main__':
    print('ХЭШ:\n1 - ',hsh[0],'\n2 - ',hsh[1],'\n3 - ',hsh[2])
    A = int(input('>>> '))
    B = int(input('1- однопоточный 2- многопотчный\n>>  '))
    if B == 1:
        start_time = datetime.now()
        brute_force1('*****', hsh[A-1], verbose=True)
        print('Время обработки = ', datetime.now() - start_time)
    elif B==2:
        start_time = datetime.now()
        passw_bytes = brute_force2(b'*****', binascii.unhexlify(hsh[A-1]))
        print('паролль = ',passw_bytes.decode())
        print('Время обработки = ', datetime.now() - start_time)



