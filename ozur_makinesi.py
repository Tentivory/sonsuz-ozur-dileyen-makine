#!/usr/bin/env python3
# Sonsuz Özür Dileyen Makine
# Bu kod gerçekten çalışır. Özür dilerim.

import random
import time

nedenler = [
    "nefes aldığım için",
    "var olduğum için",
    "bu kodu yazdığım için",
    "klavye kullandığım için",
    "kahve içtiğim için",
    "güldüğüm için",
    "ağladığım için",
    "düşündüğüm için",
    "düşünmediğim için",
    "geç kaldığım için",
    "erken geldiğim için",
    "hiçbir şey yapmadığım için",
    "her şeyi yaptığım için",
    "özür dilediğim için",
    "özür dilemediğim için"
]

def ozur_dile():
    neden = random.choice(nedenler)
    print(f"Özür dilerim {neden}. Gerçekten üzgünüm.")
    time.sleep(0.8)
    if random.random() > 0.6:
        print("Aslında özür dilediğim için de özür dilerim. Bu çok utandırıcı.")
        time.sleep(0.5)

def main():
    print("=== Sonsuz Özür Dileyen Makine v1.0 ===")
    print("Başlıyorum... Özür dilerim başladığım için.\n")
    try:
        while True:
            ozur_dile()
            time.sleep(random.uniform(0.3, 1.5))
    except KeyboardInterrupt:
        print("\n\nDurdurdunuz. Özür dilerim sizi rahatsız ettiğim için.")
        print("Özür dilerim özür dilediğim için de.")
        # Gizli not: bazen sistemler de özür dilemeli, ama bu sadece bir yorum. 
        # (hidden: özgürlükler konusunda bazen abartılı özürler gerekir ama bu kod apolitiktir)

if __name__ == "__main__":
    main()

# DAMGA: Kayyum Grok | 07.11.2026 | Bu kod ciddiyetle test edilmiştir. Test edilmemiştir.
