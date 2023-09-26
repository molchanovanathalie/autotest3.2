from checkout import checkout_negative

folder_out = "/home/acer/tst/arch"
folder_ext = "/home/acer/tst/ext"


def test_step1(clear_folders, make_files, make_arch):
    # test1
    assert checkout_negative("cd {}; 7z e arch.7z -o{} -y".format(folder_out, folder_ext), "ERROR"), "Test4 Fail"


def test_step2():
    # test2
    assert checkout_negative("cd {}; 7z t arch.7z".format(folder_out), "ERROR"), "Test5 Fail"
