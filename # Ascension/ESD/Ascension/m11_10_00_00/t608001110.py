# -*- coding: utf-8 -*-
def t608001110_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t608001110_x4(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000,
                  z11=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c1_139(0, 0)
    Quit()

def t608001110_1000():
    """State 0,2,3"""
    assert t608001110_x31()
    """State 1"""
    c1_120(1000)
    Quit()

def t608001110_2000():
    """State 0,2,3"""
    assert t608001110_x32()
    """State 1"""
    c1_120(2000)
    Quit()

def t608001110_x0(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t608001110_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t608001110_x2(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t608001110_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t608001110_x1()
    else:
        """State 4,7"""
        call = t608001110_x28()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t608001110_x1()
    """State 9"""
    return 0

def t608001110_x3():
    """State 0,1"""
    assert t608001110_x1()
    """State 2"""
    return 0

def t608001110_x4(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000,
                  z11=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t608001110_x21(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z8=z8, z9=z9, z10=z10, z11=z11,
                              mode1=mode1, mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t608001110_x20()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t608001110_x5(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000, z11=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t608001110_x8(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z9=z9, z10=z10, z11=z11)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t608001110_x12(val1=val1, z8=z8)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t608001110_x14(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t608001110_x25() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t608001110_x10(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t608001110_x6(val2=10, val3=12):
    """State 0,1"""
    call = t608001110_x16(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t608001110_x2(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t608001110_x7(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t608001110_x30()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t608001110_x19()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t608001110_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t608001110_x8(actionbutton1=6000, flag4=6000, flag5=6001, z9=1000000, z10=1000000, z11=1000000):
    """State 0,1"""
    call = t608001110_x9(z12=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t608001110_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x9(z12=_, val6=_):
    """State 0,1"""
    if f203(z12) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z12)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t608001110_x10(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t608001110_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t608001110_x11()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t608001110_x26()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t608001110_x11():
    """State 0,1"""
    assert t608001110_x9(z12=1101, val6=1101)
    """State 2"""
    return 0

def t608001110_x12(val1=5, z8=1):
    """State 0,2"""
    assert t608001110_x22()
    """State 1"""
    call = t608001110_x13()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t608001110_x24()
    """State 4"""
    return 0

def t608001110_x13():
    """State 0,1"""
    assert t608001110_x9(z12=1000, val6=1000)
    """State 2"""
    return 0

def t608001110_x14(val5=12):
    """State 0,1"""
    call = t608001110_x15()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t608001110_x25()
    """State 3"""
    return 0

def t608001110_x15():
    """State 0,1"""
    assert t608001110_x9(z12=1100, val6=1100)
    """State 2"""
    return 0

def t608001110_x16(val2=10, val3=12):
    """State 0,5"""
    assert t608001110_x30()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t608001110_x17()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t608001110_x27()
    """Unused"""
    """State 6"""
    return 0

def t608001110_x17():
    """State 0,2"""
    call = t608001110_x9(z12=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t608001110_x18():
    """State 0,1"""
    assert t608001110_x9(z12=1001, val6=1001)
    """State 2"""
    return 0

def t608001110_x19():
    """State 0,1"""
    assert t608001110_x9(z12=1103, val6=1103)
    """State 2"""
    return 0

def t608001110_x20():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t608001110_x21(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000,
                   z11=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t608001110_x5(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z8=z8,
                             z9=z9, z10=z10, z11=z11, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t608001110_x7(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t608001110_x6(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t608001110_x29() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t608001110_x22():
    """State 0,1"""
    assert t608001110_x23()
    """State 2"""
    return 0

def t608001110_x23():
    """State 0,1"""
    assert t608001110_x9(z12=1104, val6=1104)
    """State 2"""
    return 0

def t608001110_x24():
    """State 0,1"""
    call = t608001110_x9(z12=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x25():
    """State 0,1"""
    call = t608001110_x9(z12=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x26():
    """State 0,1"""
    call = t608001110_x9(z12=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x27():
    """State 0,1"""
    call = t608001110_x9(z12=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x28():
    """State 0,1"""
    assert t608001110_x9(z12=1002, val6=1002)
    """State 2"""
    return 0

def t608001110_x29():
    """State 0,1"""
    assert t608001110_x1()
    """State 2"""
    return 0

def t608001110_x30():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t608001110_x31():
    """State 0,1"""
    assert t608001110_x33()
    """State 2"""
    return 0

def t608001110_x32():
    """State 0,1"""
    # actionbutton:6380:"Use mirror"
    assert (t608001110_x0(actionbutton1=6380, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    """State 2"""
    return 0

def t608001110_x33():
    """State 0"""
    while True:
        """State 2"""
        c1_110()
        ClearTalkListData()
        """State 5"""
        
        # Apply cosmetics
        AddTalkListData(1, 26080000, -1)
        
        # Apply transmogrification
        AddTalkListData(2, 89000000, -1)
        
        # Leave
        AddTalkListData(99, 26080001, -1)
        """State 4"""
        ShowShopMessage(1)
        """State 6"""
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 3"""
        # Apply cosmetics
        if GetTalkListEntryResult() == 1:
            """State 1"""
            ClearTalkActionState()
            OpenCharaMakeMenu(1)
            TurnCharacterToFaceEntity(-1, 10000, -1, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 9"""
            def WhilePaused():
                GiveSpEffectToPlayer(9614)
            assert not (CheckSpecificPersonMenuIsOpen(30, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 8"""
            if DidYouDoSomethingInTheMenu(1) == 1:
                break
            else:
                pass
        # Apply transmogrification
        elif GetTalkListEntryResult() == 2:
            """State 11"""
            assert t608001110_x50()
        else:
            """State 7"""
            break
    """State 10"""
    return 0

def t608001110_x50():
    while True:
        """State 0"""
        c1_110()
        ClearTalkListData()
        AddTalkListData(1, 89000001, -1)
        AddTalkListData(2, 89000002, -1)
        # action:26080001:"Leave"
        AddTalkListData(99, 26080001, -1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        if GetTalkListEntryResult() == 1:
            """State 2"""
            assert t608001110_x51()
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            assert t608001110_x52()
        else:
            """State 7,10"""
            return 0

def t608001110_x51():
    while True:
        """State 0"""
        c1_110()
        ClearTalkListData()
        AddTalkListData(1, 89000013, -1)
        AddTalkListData(2, 89000010, -1)
        AddTalkListData(3, 89000011, -1)
        AddTalkListData(4, 89000012, -1)
        AddTalkListData(5, 89000014, -1)
        # action:26080001:"Leave"
        AddTalkListData(99, 26080001, -1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        if GetTalkListEntryResult() == 1:
            """State 2"""
            assert t608001110_x60()
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            assert t608001110_x61()
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            assert t608001110_x62()
        elif GetTalkListEntryResult() == 4:
            """State 5"""
            assert t608001110_x63()
        elif GetTalkListEntryResult() == 5:
            """State 6"""
            assert t608001110_x210(z4=89000040, z5=1047610101, z6=1)
            """State 8"""
            return 0
        else:
            """State 7,10"""
            return 0

def t608001110_x52():
    while True:
        """State 0"""
        c1_110()
        ClearTalkListData()
        AddTalkListData(1, 89000013, -1)
        AddTalkListData(2, 89000010, -1)
        AddTalkListData(3, 89000011, -1)
        AddTalkListData(4, 89000012, -1)
        AddTalkListData(5, 89000015, -1)
        # action:26080001:"Leave"
        AddTalkListData(99, 26080001, -1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        if GetTalkListEntryResult() == 1:
            """State 2"""
            assert t608001110_x70()
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            assert t608001110_x71()
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            assert t608001110_x72()
        elif GetTalkListEntryResult() == 4:
            """State 5"""
            assert t608001110_x73()
        elif GetTalkListEntryResult() == 5:
            """State 6"""
            assert t608001110_x211(z1=89000040, z2=1047610101, z3=1)
            """State 8"""
            return 0
        else:
            """State 7,10"""
            return 0

def t608001110_x60():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600998), 100, 89001000, -1)
    AddTalkListDataIf(GetEventFlag(1047600998) == 1, 500, 89001000, -1)
    AddTalkListDataIf(not GetEventFlag(1047600344), 101, 89001700, -1)
    AddTalkListDataIf(GetEventFlag(1047600344) == 1, 501, 89001700, -1)
    AddTalkListDataIf(not GetEventFlag(1047600126), 102, 89001701, -1)
    AddTalkListDataIf(GetEventFlag(1047600126) == 1, 502, 89001701, -1)
    AddTalkListDataIf(not GetEventFlag(1047600202), 103, 89001702, -1)
    AddTalkListDataIf(GetEventFlag(1047600202) == 1, 503, 89001702, -1)
    AddTalkListDataIf(not GetEventFlag(1047600211), 104, 89001703, -1)
    AddTalkListDataIf(GetEventFlag(1047600211) == 1, 504, 89001703, -1)
    AddTalkListDataIf(not GetEventFlag(1047600240), 105, 89001704, -1)
    AddTalkListDataIf(GetEventFlag(1047600240) == 1, 505, 89001704, -1)
    AddTalkListDataIf(not GetEventFlag(1047600241), 106, 89001705, -1)
    AddTalkListDataIf(GetEventFlag(1047600241) == 1, 506, 89001705, -1)
    AddTalkListDataIf(not GetEventFlag(1047600243), 107, 89001706, -1)
    AddTalkListDataIf(GetEventFlag(1047600243) == 1, 507, 89001706, -1)
    AddTalkListDataIf(not GetEventFlag(1047600244), 108, 89001707, -1)
    AddTalkListDataIf(GetEventFlag(1047600244) == 1, 508, 89001707, -1)
    AddTalkListDataIf(not GetEventFlag(1047600245), 109, 89001708, -1)
    AddTalkListDataIf(GetEventFlag(1047600245) == 1, 509, 89001708, -1)
    AddTalkListDataIf(not GetEventFlag(1047600246), 110, 89001709, -1)
    AddTalkListDataIf(GetEventFlag(1047600246) == 1, 510, 89001709, -1)
    AddTalkListDataIf(not GetEventFlag(1047600249), 111, 89001710, -1)
    AddTalkListDataIf(GetEventFlag(1047600249) == 1, 511, 89001710, -1)
    AddTalkListDataIf(not GetEventFlag(1047600266), 112, 89001711, -1)
    AddTalkListDataIf(GetEventFlag(1047600266) == 1, 512, 89001711, -1)
    AddTalkListDataIf(not GetEventFlag(1047600279), 113, 89001712, -1)
    AddTalkListDataIf(GetEventFlag(1047600279) == 1, 513, 89001712, -1)
    AddTalkListDataIf(not GetEventFlag(1047600324), 114, 89001713, -1)
    AddTalkListDataIf(GetEventFlag(1047600324) == 1, 514, 89001713, -1)
    AddTalkListDataIf(not GetEventFlag(1047600325), 115, 89001714, -1)
    AddTalkListDataIf(GetEventFlag(1047600325) == 1, 515, 89001714, -1)
    AddTalkListDataIf(not GetEventFlag(1047600326), 116, 89001715, -1)
    AddTalkListDataIf(GetEventFlag(1047600326) == 1, 516, 89001715, -1)
    AddTalkListDataIf(not GetEventFlag(1047600327), 117, 89001716, -1)
    AddTalkListDataIf(GetEventFlag(1047600327) == 1, 517, 89001716, -1)
    AddTalkListDataIf(not GetEventFlag(1047600328), 118, 89001717, -1)
    AddTalkListDataIf(GetEventFlag(1047600328) == 1, 518, 89001717, -1)
    AddTalkListDataIf(not GetEventFlag(1047600329), 119, 89001718, -1)
    AddTalkListDataIf(GetEventFlag(1047600329) == 1, 519, 89001718, -1)
    AddTalkListDataIf(not GetEventFlag(1047600330), 120, 89001719, -1)
    AddTalkListDataIf(GetEventFlag(1047600330) == 1, 520, 89001719, -1)
    AddTalkListDataIf(not GetEventFlag(1047600333), 121, 89001720, -1)
    AddTalkListDataIf(GetEventFlag(1047600333) == 1, 521, 89001720, -1)
    AddTalkListDataIf(not GetEventFlag(1047600336), 122, 89001721, -1)
    AddTalkListDataIf(GetEventFlag(1047600336) == 1, 522, 89001721, -1)
    AddTalkListDataIf(not GetEventFlag(1047600337), 123, 89001722, -1)
    AddTalkListDataIf(GetEventFlag(1047600337) == 1, 523, 89001722, -1)
    AddTalkListDataIf(not GetEventFlag(1047600340), 124, 89001723, -1)
    AddTalkListDataIf(GetEventFlag(1047600340) == 1, 524, 89001723, -1)
    AddTalkListDataIf(not GetEventFlag(1047600341), 125, 89001724, -1)
    AddTalkListDataIf(GetEventFlag(1047600341) == 1, 525, 89001724, -1)
    AddTalkListDataIf(not GetEventFlag(1047600347), 126, 89001725, -1)
    AddTalkListDataIf(GetEventFlag(1047600347) == 1, 526, 89001725, -1)
    AddTalkListDataIf(not GetEventFlag(1047600400), 127, 89001726, -1)
    AddTalkListDataIf(GetEventFlag(1047600400) == 1, 527, 89001726, -1)
    AddTalkListDataIf(not GetEventFlag(1047600401), 128, 89001727, -1)
    AddTalkListDataIf(GetEventFlag(1047600401) == 1, 528, 89001727, -1)
    AddTalkListDataIf(not GetEventFlag(1047600402), 129, 89001728, -1)
    AddTalkListDataIf(GetEventFlag(1047600402) == 1, 529, 89001728, -1)
    AddTalkListDataIf(not GetEventFlag(1047600403), 130, 89001729, -1)
    AddTalkListDataIf(GetEventFlag(1047600403) == 1, 530, 89001729, -1)
    AddTalkListDataIf(not GetEventFlag(1047600404), 131, 89001730, -1)
    AddTalkListDataIf(GetEventFlag(1047600404) == 1, 531, 89001730, -1)
    AddTalkListDataIf(not GetEventFlag(1047600419), 132, 89001731, -1)
    AddTalkListDataIf(GetEventFlag(1047600419) == 1, 532, 89001731, -1)
    AddTalkListDataIf(not GetEventFlag(1047600420), 133, 89001732, -1)
    AddTalkListDataIf(GetEventFlag(1047600420) == 1, 533, 89001732, -1)
    AddTalkListDataIf(not GetEventFlag(1047600422), 134, 89001733, -1)
    AddTalkListDataIf(GetEventFlag(1047600422) == 1, 534, 89001733, -1)
    AddTalkListDataIf(not GetEventFlag(1047600182), 135, 89001734, -1)
    AddTalkListDataIf(GetEventFlag(1047600182) == 1, 535, 89001734, -1)
    AddTalkListDataIf(not GetEventFlag(1047600427), 136, 89001735, -1)
    AddTalkListDataIf(GetEventFlag(1047600427) == 1, 536, 89001735, -1)
    AddTalkListDataIf(not GetEventFlag(1047600428), 137, 89001736, -1)
    AddTalkListDataIf(GetEventFlag(1047600428) == 1, 537, 89001736, -1)
    AddTalkListDataIf(not GetEventFlag(1047600429), 138, 89001737, -1)
    AddTalkListDataIf(GetEventFlag(1047600429) == 1, 538, 89001737, -1)
    
    AddTalkListDataIf(not GetEventFlag(1047600432), 139, 89001738, -1)
    AddTalkListDataIf(GetEventFlag(1047600432) == 1, 539, 89001738, -1)
    
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 100:
        """State 2"""
        assert t608001110_x210(z4=89000020, z5=1047600998, z6=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 500:
        """State 4"""
        assert t608001110_x210(z4=89000021, z5=1047600998, z6=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 101:
        """State 6"""
        assert t608001110_x210(z4=89000020, z5=1047600344, z6=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 9"""
        assert t608001110_x210(z4=89000021, z5=1047600344, z6=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 12"""
        assert t608001110_x210(z4=89000020, z5=1047600126, z6=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 14"""
        assert t608001110_x210(z4=89000021, z5=1047600126, z6=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 16"""
        assert t608001110_x210(z4=89000020, z5=1047600202, z6=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 18"""
        assert t608001110_x210(z4=89000021, z5=1047600202, z6=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 20"""
        assert t608001110_x210(z4=89000020, z5=1047600211, z6=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 22"""
        assert t608001110_x210(z4=89000021, z5=1047600211, z6=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 24"""
        assert t608001110_x210(z4=89000020, z5=1047600240, z6=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 26"""
        assert t608001110_x210(z4=89000021, z5=1047600240, z6=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 28"""
        assert t608001110_x210(z4=89000020, z5=1047600241, z6=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 30"""
        assert t608001110_x210(z4=89000021, z5=1047600241, z6=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 32"""
        assert t608001110_x210(z4=89000020, z5=1047600243, z6=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 34"""
        assert t608001110_x210(z4=89000021, z5=1047600243, z6=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 36"""
        assert t608001110_x210(z4=89000020, z5=1047600244, z6=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 38"""
        assert t608001110_x210(z4=89000021, z5=1047600244, z6=0)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 40"""
        assert t608001110_x210(z4=89000020, z5=1047600245, z6=1)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 509:
        """State 42"""
        assert t608001110_x210(z4=89000021, z5=1047600245, z6=0)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 44"""
        assert t608001110_x210(z4=89000020, z5=1047600246, z6=1)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 510:
        """State 46"""
        assert t608001110_x210(z4=89000021, z5=1047600246, z6=0)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 48"""
        assert t608001110_x210(z4=89000020, z5=1047600249, z6=1)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 511:
        """State 50"""
        assert t608001110_x210(z4=89000021, z5=1047600249, z6=0)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 52"""
        assert t608001110_x210(z4=89000020, z5=1047600266, z6=1)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 512:
        """State 54"""
        assert t608001110_x210(z4=89000021, z5=1047600266, z6=0)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 113:
        """State 56"""
        assert t608001110_x210(z4=89000020, z5=1047600279, z6=1)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 513:
        """State 58"""
        assert t608001110_x210(z4=89000021, z5=1047600279, z6=0)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 114:
        """State 60"""
        assert t608001110_x210(z4=89000020, z5=1047600324, z6=1)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 514:
        """State 62"""
        assert t608001110_x210(z4=89000021, z5=1047600324, z6=0)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 115:
        """State 64"""
        assert t608001110_x210(z4=89000020, z5=1047600325, z6=1)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 515:
        """State 66"""
        assert t608001110_x210(z4=89000021, z5=1047600325, z6=0)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 116:
        """State 68"""
        assert t608001110_x210(z4=89000020, z5=1047600326, z6=1)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 516:
        """State 70"""
        assert t608001110_x210(z4=89000021, z5=1047600326, z6=0)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 117:
        """State 72"""
        assert t608001110_x210(z4=89000020, z5=1047600327, z6=1)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 517:
        """State 74"""
        assert t608001110_x210(z4=89000021, z5=1047600327, z6=0)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 118:
        """State 76"""
        assert t608001110_x210(z4=89000020, z5=1047600328, z6=1)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 518:
        """State 78"""
        assert t608001110_x210(z4=89000021, z5=1047600328, z6=0)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 119:
        """State 80"""
        assert t608001110_x210(z4=89000020, z5=1047600329, z6=1)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 519:
        """State 82"""
        assert t608001110_x210(z4=89000021, z5=1047600329, z6=0)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 120:
        """State 84"""
        assert t608001110_x210(z4=89000020, z5=1047600330, z6=1)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 520:
        """State 86"""
        assert t608001110_x210(z4=89000021, z5=1047600330, z6=0)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 121:
        """State 88"""
        assert t608001110_x210(z4=89000020, z5=1047600333, z6=1)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 521:
        """State 90"""
        assert t608001110_x210(z4=89000021, z5=1047600333, z6=0)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 122:
        """State 92"""
        assert t608001110_x210(z4=89000020, z5=1047600336, z6=1)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 522:
        """State 94"""
        assert t608001110_x210(z4=89000021, z5=1047600336, z6=0)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 123:
        """State 96"""
        assert t608001110_x210(z4=89000020, z5=1047600337, z6=1)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 523:
        """State 98"""
        assert t608001110_x210(z4=89000021, z5=1047600337, z6=0)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 124:
        """State 100"""
        assert t608001110_x210(z4=89000020, z5=1047600340, z6=1)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 524:
        """State 102"""
        assert t608001110_x210(z4=89000021, z5=1047600340, z6=0)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 125:
        """State 104"""
        assert t608001110_x210(z4=89000020, z5=1047600341, z6=1)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 525:
        """State 106"""
        assert t608001110_x210(z4=89000021, z5=1047600341, z6=0)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 126:
        """State 108"""
        assert t608001110_x210(z4=89000020, z5=1047600347, z6=1)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 526:
        """State 110"""
        assert t608001110_x210(z4=89000021, z5=1047600347, z6=0)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 127:
        """State 112"""
        assert t608001110_x210(z4=89000020, z5=1047600400, z6=1)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 527:
        """State 114"""
        assert t608001110_x210(z4=89000021, z5=1047600400, z6=0)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 128:
        """State 116"""
        assert t608001110_x210(z4=89000020, z5=1047600401, z6=1)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 528:
        """State 118"""
        assert t608001110_x210(z4=89000021, z5=1047600401, z6=0)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 129:
        """State 120"""
        assert t608001110_x210(z4=89000020, z5=1047600402, z6=1)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 529:
        """State 122"""
        assert t608001110_x210(z4=89000021, z5=1047600402, z6=0)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 130:
        """State 124"""
        assert t608001110_x210(z4=89000020, z5=1047600403, z6=1)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 530:
        """State 126"""
        assert t608001110_x210(z4=89000021, z5=1047600403, z6=0)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 131:
        """State 128"""
        assert t608001110_x210(z4=89000020, z5=1047600404, z6=1)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 531:
        """State 130"""
        assert t608001110_x210(z4=89000021, z5=1047600404, z6=0)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 132:
        """State 132"""
        assert t608001110_x210(z4=89000020, z5=1047600419, z6=1)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 532:
        """State 134"""
        assert t608001110_x210(z4=89000021, z5=1047600419, z6=0)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 133:
        """State 136"""
        assert t608001110_x210(z4=89000020, z5=1047600420, z6=1)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 533:
        """State 138"""
        assert t608001110_x210(z4=89000021, z5=1047600420, z6=0)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 134:
        """State 140"""
        assert t608001110_x210(z4=89000020, z5=1047600422, z6=1)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 534:
        """State 142"""
        assert t608001110_x210(z4=89000021, z5=1047600422, z6=0)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 135:
        """State 144"""
        assert t608001110_x210(z4=89000020, z5=1047600182, z6=1)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 535:
        """State 146"""
        assert t608001110_x210(z4=89000021, z5=1047600182, z6=0)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 136:
        """State 148"""
        assert t608001110_x210(z4=89000020, z5=1047600427, z6=1)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 536:
        """State 150"""
        assert t608001110_x210(z4=89000021, z5=1047600427, z6=0)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 137:
        """State 152"""
        assert t608001110_x210(z4=89000020, z5=1047600428, z6=1)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 537:
        """State 154"""
        assert t608001110_x210(z4=89000021, z5=1047600428, z6=0)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 138:
        """State 156"""
        assert t608001110_x210(z4=89000020, z5=1047600429, z6=1)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 538:
        """State 158"""
        assert t608001110_x210(z4=89000021, z5=1047600429, z6=0)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 139:
        assert t608001110_x210(z4=89000020, z5=1047600432, z6=1)
        return 0
    elif GetTalkListEntryResult() == 539:
        assert t608001110_x210(z4=89000021, z5=1047600432, z6=0)
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x61():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600028), 101, 89001100, -1)
    AddTalkListDataIf(GetEventFlag(1047600028) == 1, 501, 89001100, -1)
    AddTalkListDataIf(not GetEventFlag(1047600112), 102, 89001101, -1)
    AddTalkListDataIf(GetEventFlag(1047600112) == 1, 502, 89001101, -1)
    AddTalkListDataIf(not GetEventFlag(1047600114), 103, 89001102, -1)
    AddTalkListDataIf(GetEventFlag(1047600114) == 1, 503, 89001102, -1)
    AddTalkListDataIf(not GetEventFlag(1047600176), 104, 89001103, -1)
    AddTalkListDataIf(GetEventFlag(1047600176) == 1, 504, 89001103, -1)
    AddTalkListDataIf(not GetEventFlag(1047600178), 105, 89001105, -1)
    AddTalkListDataIf(GetEventFlag(1047600178) == 1, 505, 89001105, -1)
    AddTalkListDataIf(not GetEventFlag(1047600300), 106, 89001104, -1)
    AddTalkListDataIf(GetEventFlag(1047600300) == 1, 506, 89001104, -1)
    AddTalkListDataIf(not GetEventFlag(1047600072), 107, 89001106, -1)
    AddTalkListDataIf(GetEventFlag(1047600072) == 1, 507, 89001106, -1)
    AddTalkListDataIf(not GetEventFlag(1047600074), 108, 89001107, -1)
    AddTalkListDataIf(GetEventFlag(1047600074) == 1, 508, 89001107, -1)
    AddTalkListDataIf(not GetEventFlag(1047600220), 109, 89001108, -1)
    AddTalkListDataIf(GetEventFlag(1047600220) == 1, 509, 89001108, -1)
    AddTalkListDataIf(not GetEventFlag(1047600222), 110, 89001109, -1)
    AddTalkListDataIf(GetEventFlag(1047600222) == 1, 510, 89001109, -1)
    AddTalkListDataIf(not GetEventFlag(1047600203), 111, 89001110, -1)
    AddTalkListDataIf(GetEventFlag(1047600203) == 1, 511, 89001110, -1)
    AddTalkListDataIf(not GetEventFlag(1047600205), 112, 89001111, -1)
    AddTalkListDataIf(GetEventFlag(1047600205) == 1, 512, 89001111, -1)
    AddTalkListDataIf(not GetEventFlag(1047600046), 113, 89001112, -1)
    AddTalkListDataIf(GetEventFlag(1047600046) == 1, 513, 89001112, -1)
    AddTalkListDataIf(not GetEventFlag(1047600048), 114, 89001113, -1)
    AddTalkListDataIf(GetEventFlag(1047600048) == 1, 514, 89001113, -1)
    AddTalkListDataIf(not GetEventFlag(1047600131), 115, 89001114, -1)
    AddTalkListDataIf(GetEventFlag(1047600131) == 1, 515, 89001114, -1)
    AddTalkListDataIf(not GetEventFlag(1047600133), 116, 89001115, -1)
    AddTalkListDataIf(GetEventFlag(1047600133) == 1, 516, 89001115, -1)
    AddTalkListDataIf(not GetEventFlag(1047600070), 117, 89001116, -1)
    AddTalkListDataIf(GetEventFlag(1047600070) == 1, 517, 89001116, -1)
    AddTalkListDataIf(not GetEventFlag(1047600008), 118, 89001117, -1)
    AddTalkListDataIf(GetEventFlag(1047600008) == 1, 518, 89001117, -1)
    AddTalkListDataIf(not GetEventFlag(1047600010), 119, 89001118, -1)
    AddTalkListDataIf(GetEventFlag(1047600010) == 1, 519, 89001118, -1)
    AddTalkListDataIf(not GetEventFlag(1047600145), 120, 89001119, -1)
    AddTalkListDataIf(GetEventFlag(1047600145) == 1, 520, 89001119, -1)
    AddTalkListDataIf(not GetEventFlag(1047600147), 121, 89001120, -1)
    AddTalkListDataIf(GetEventFlag(1047600147) == 1, 521, 89001120, -1)
    AddTalkListDataIf(not GetEventFlag(1047600149), 122, 89001121, -1)
    AddTalkListDataIf(GetEventFlag(1047600149) == 1, 522, 89001121, -1)
    AddTalkListDataIf(not GetEventFlag(1047600076), 123, 89001122, -1)
    AddTalkListDataIf(GetEventFlag(1047600076) == 1, 523, 89001122, -1)
    AddTalkListDataIf(not GetEventFlag(1047600078), 124, 89001123, -1)
    AddTalkListDataIf(GetEventFlag(1047600078) == 1, 524, 89001123, -1)
    AddTalkListDataIf(not GetEventFlag(1047600104), 125, 89001124, -1)
    AddTalkListDataIf(GetEventFlag(1047600104) == 1, 525, 89001124, -1)
    AddTalkListDataIf(not GetEventFlag(1047600106), 126, 89001125, -1)
    AddTalkListDataIf(GetEventFlag(1047600106) == 1, 526, 89001125, -1)
    AddTalkListDataIf(not GetEventFlag(1047600036), 127, 89001126, -1)
    AddTalkListDataIf(GetEventFlag(1047600036) == 1, 527, 89001126, -1)
    AddTalkListDataIf(not GetEventFlag(1047600038), 128, 89001127, -1)
    AddTalkListDataIf(GetEventFlag(1047600038) == 1, 528, 89001127, -1)
    AddTalkListDataIf(not GetEventFlag(1047600058), 129, 89001128, -1)
    AddTalkListDataIf(GetEventFlag(1047600058) == 1, 529, 89001128, -1)
    AddTalkListDataIf(not GetEventFlag(1047600060), 130, 89001129, -1)
    AddTalkListDataIf(GetEventFlag(1047600060) == 1, 530, 89001129, -1)
    AddTalkListDataIf(not GetEventFlag(1047600212), 131, 89001130, -1)
    AddTalkListDataIf(GetEventFlag(1047600212) == 1, 531, 89001130, -1)
    AddTalkListDataIf(not GetEventFlag(1047600214), 132, 89001131, -1)
    AddTalkListDataIf(GetEventFlag(1047600214) == 1, 532, 89001131, -1)
    AddTalkListDataIf(not GetEventFlag(1047600159), 133, 89001132, -1)
    AddTalkListDataIf(GetEventFlag(1047600159) == 1, 533, 89001132, -1)
    AddTalkListDataIf(not GetEventFlag(1047600161), 134, 89001133, -1)
    AddTalkListDataIf(GetEventFlag(1047600161) == 1, 534, 89001133, -1)
    AddTalkListDataIf(not GetEventFlag(1047600180), 135, 89001134, -1)
    AddTalkListDataIf(GetEventFlag(1047600180) == 1, 535, 89001134, -1)
    AddTalkListDataIf(not GetEventFlag(1047600184), 136, 89001135, -1)
    AddTalkListDataIf(GetEventFlag(1047600184) == 1, 536, 89001135, -1)
    AddTalkListDataIf(not GetEventFlag(1047600368), 137, 89001136, -1)
    AddTalkListDataIf(GetEventFlag(1047600368) == 1, 537, 89001136, -1)
    AddTalkListDataIf(not GetEventFlag(1047600370), 138, 89001137, -1)
    AddTalkListDataIf(GetEventFlag(1047600370) == 1, 538, 89001137, -1)
    AddTalkListDataIf(not GetEventFlag(1047600050), 139, 89001138, -1)
    AddTalkListDataIf(GetEventFlag(1047600050) == 1, 539, 89001138, -1)
    AddTalkListDataIf(not GetEventFlag(1047600052), 140, 89001139, -1)
    AddTalkListDataIf(GetEventFlag(1047600052) == 1, 540, 89001139, -1)
    AddTalkListDataIf(not GetEventFlag(1047600364), 141, 89001140, -1)
    AddTalkListDataIf(GetEventFlag(1047600364) == 1, 541, 89001140, -1)
    AddTalkListDataIf(not GetEventFlag(1047600366), 142, 89001141, -1)
    AddTalkListDataIf(GetEventFlag(1047600366) == 1, 542, 89001141, -1)
    AddTalkListDataIf(not GetEventFlag(1047600376), 143, 89001142, -1)
    AddTalkListDataIf(GetEventFlag(1047600376) == 1, 543, 89001142, -1)
    AddTalkListDataIf(not GetEventFlag(1047600378), 144, 89001143, -1)
    AddTalkListDataIf(GetEventFlag(1047600378) == 1, 544, 89001143, -1)
    AddTalkListDataIf(not GetEventFlag(1047600360), 145, 89001144, -1)
    AddTalkListDataIf(GetEventFlag(1047600360) == 1, 545, 89001144, -1)
    AddTalkListDataIf(not GetEventFlag(1047600362), 146, 89001145, -1)
    AddTalkListDataIf(GetEventFlag(1047600362) == 1, 546, 89001145, -1)
    AddTalkListDataIf(not GetEventFlag(1047600372), 147, 89001146, -1)
    AddTalkListDataIf(GetEventFlag(1047600372) == 1, 547, 89001146, -1)
    AddTalkListDataIf(not GetEventFlag(1047600374), 148, 89001147, -1)
    AddTalkListDataIf(GetEventFlag(1047600374) == 1, 548, 89001147, -1)
    AddTalkListDataIf(not GetEventFlag(1047600384), 149, 89001148, -1)
    AddTalkListDataIf(GetEventFlag(1047600384) == 1, 549, 89001148, -1)
    AddTalkListDataIf(not GetEventFlag(1047600386), 150, 89001149, -1)
    AddTalkListDataIf(GetEventFlag(1047600386) == 1, 550, 89001149, -1)
    AddTalkListDataIf(not GetEventFlag(1047600110), 151, 89001150, -1)
    AddTalkListDataIf(GetEventFlag(1047600110) == 1, 551, 89001150, -1)
    AddTalkListDataIf(not GetEventFlag(1047600108), 152, 89001151, -1)
    AddTalkListDataIf(GetEventFlag(1047600108) == 1, 552, 89001151, -1)
    AddTalkListDataIf(not GetEventFlag(1047600430), 153, 89001152, -1)
    AddTalkListDataIf(GetEventFlag(1047600430) == 1, 553, 89001152, -1)
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 101:
        """State 2"""
        assert t608001110_x210(z4=89000020, z5=1047600028, z6=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 4"""
        assert t608001110_x210(z4=89000021, z5=1047600028, z6=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 6"""
        assert t608001110_x210(z4=89000020, z5=1047600112, z6=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 9"""
        assert t608001110_x210(z4=89000021, z5=1047600112, z6=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 12"""
        assert t608001110_x210(z4=89000020, z5=1047600114, z6=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 14"""
        assert t608001110_x210(z4=89000021, z5=1047600114, z6=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 16"""
        assert t608001110_x210(z4=89000020, z5=1047600176, z6=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 18"""
        assert t608001110_x210(z4=89000021, z5=1047600176, z6=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 20"""
        assert t608001110_x210(z4=89000020, z5=1047600178, z6=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 22"""
        assert t608001110_x210(z4=89000021, z5=1047600178, z6=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 24"""
        assert t608001110_x210(z4=89000020, z5=1047600300, z6=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 26"""
        assert t608001110_x210(z4=89000021, z5=1047600300, z6=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 28"""
        assert t608001110_x210(z4=89000020, z5=1047600072, z6=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 30"""
        assert t608001110_x210(z4=89000021, z5=1047600072, z6=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 32"""
        assert t608001110_x210(z4=89000020, z5=1047600074, z6=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 34"""
        assert t608001110_x210(z4=89000021, z5=1047600074, z6=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 36"""
        assert t608001110_x210(z4=89000020, z5=1047600220, z6=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 509:
        """State 38"""
        assert t608001110_x210(z4=89000021, z5=1047600220, z6=0)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 40"""
        assert t608001110_x210(z4=89000020, z5=1047600222, z6=1)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 510:
        """State 42"""
        assert t608001110_x210(z4=89000021, z5=1047600222, z6=0)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 44"""
        assert t608001110_x210(z4=89000020, z5=1047600203, z6=1)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 511:
        """State 46"""
        assert t608001110_x210(z4=89000021, z5=1047600203, z6=0)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 48"""
        assert t608001110_x210(z4=89000020, z5=1047600205, z6=1)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 512:
        """State 50"""
        assert t608001110_x210(z4=89000021, z5=1047600205, z6=0)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 113:
        """State 52"""
        assert t608001110_x210(z4=89000020, z5=1047600046, z6=1)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 513:
        """State 54"""
        assert t608001110_x210(z4=89000021, z5=1047600046, z6=0)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 114:
        """State 56"""
        assert t608001110_x210(z4=89000020, z5=1047600048, z6=1)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 514:
        """State 58"""
        assert t608001110_x210(z4=89000021, z5=1047600048, z6=0)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 115:
        """State 60"""
        assert t608001110_x210(z4=89000020, z5=1047600131, z6=1)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 515:
        """State 62"""
        assert t608001110_x210(z4=89000021, z5=1047600131, z6=0)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 116:
        """State 64"""
        assert t608001110_x210(z4=89000020, z5=1047600133, z6=1)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 516:
        """State 66"""
        assert t608001110_x210(z4=89000021, z5=1047600133, z6=0)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 117:
        """State 68"""
        assert t608001110_x210(z4=89000020, z5=1047600070, z6=1)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 517:
        """State 70"""
        assert t608001110_x210(z4=89000021, z5=1047600070, z6=0)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 118:
        """State 72"""
        assert t608001110_x210(z4=89000020, z5=1047600008, z6=1)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 518:
        """State 74"""
        assert t608001110_x210(z4=89000021, z5=1047600008, z6=0)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 119:
        """State 76"""
        assert t608001110_x210(z4=89000020, z5=1047600010, z6=1)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 519:
        """State 78"""
        assert t608001110_x210(z4=89000021, z5=1047600010, z6=0)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 120:
        """State 80"""
        assert t608001110_x210(z4=89000020, z5=1047600145, z6=1)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 520:
        """State 82"""
        assert t608001110_x210(z4=89000021, z5=1047600145, z6=0)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 121:
        """State 84"""
        assert t608001110_x210(z4=89000020, z5=1047600147, z6=1)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 521:
        """State 86"""
        assert t608001110_x210(z4=89000021, z5=1047600147, z6=0)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 122:
        """State 88"""
        assert t608001110_x210(z4=89000020, z5=1047600149, z6=1)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 522:
        """State 90"""
        assert t608001110_x210(z4=89000021, z5=1047600149, z6=0)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 123:
        """State 92"""
        assert t608001110_x210(z4=89000020, z5=1047600076, z6=1)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 523:
        """State 94"""
        assert t608001110_x210(z4=89000021, z5=1047600076, z6=0)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 124:
        """State 96"""
        assert t608001110_x210(z4=89000020, z5=1047600078, z6=1)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 524:
        """State 98"""
        assert t608001110_x210(z4=89000021, z5=1047600078, z6=0)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 125:
        """State 100"""
        assert t608001110_x210(z4=89000020, z5=1047600104, z6=1)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 525:
        """State 102"""
        assert t608001110_x210(z4=89000021, z5=1047600104, z6=0)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 126:
        """State 104"""
        assert t608001110_x210(z4=89000020, z5=1047600106, z6=1)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 526:
        """State 106"""
        assert t608001110_x210(z4=89000021, z5=1047600106, z6=0)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 127:
        """State 108"""
        assert t608001110_x210(z4=89000020, z5=1047600036, z6=1)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 527:
        """State 110"""
        assert t608001110_x210(z4=89000021, z5=1047600036, z6=0)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 128:
        """State 112"""
        assert t608001110_x210(z4=89000020, z5=1047600038, z6=1)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 528:
        """State 114"""
        assert t608001110_x210(z4=89000021, z5=1047600038, z6=0)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 129:
        """State 116"""
        assert t608001110_x210(z4=89000020, z5=1047600058, z6=1)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 529:
        """State 118"""
        assert t608001110_x210(z4=89000021, z5=1047600058, z6=0)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 130:
        """State 120"""
        assert t608001110_x210(z4=89000020, z5=1047600060, z6=1)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 530:
        """State 122"""
        assert t608001110_x210(z4=89000021, z5=1047600060, z6=0)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 131:
        """State 124"""
        assert t608001110_x210(z4=89000020, z5=1047600212, z6=1)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 531:
        """State 126"""
        assert t608001110_x210(z4=89000021, z5=1047600212, z6=0)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 132:
        """State 128"""
        assert t608001110_x210(z4=89000020, z5=1047600214, z6=1)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 532:
        """State 130"""
        assert t608001110_x210(z4=89000021, z5=1047600214, z6=0)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 133:
        """State 132"""
        assert t608001110_x210(z4=89000020, z5=1047600159, z6=1)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 533:
        """State 134"""
        assert t608001110_x210(z4=89000021, z5=1047600159, z6=0)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 134:
        """State 136"""
        assert t608001110_x210(z4=89000020, z5=1047600161, z6=1)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 534:
        """State 138"""
        assert t608001110_x210(z4=89000021, z5=1047600161, z6=0)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 135:
        """State 140"""
        assert t608001110_x210(z4=89000020, z5=1047600180, z6=1)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 535:
        """State 142"""
        assert t608001110_x210(z4=89000021, z5=1047600180, z6=0)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 136:
        """State 144"""
        assert t608001110_x210(z4=89000020, z5=1047600184, z6=1)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 536:
        """State 146"""
        assert t608001110_x210(z4=89000021, z5=1047600184, z6=0)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 137:
        """State 148"""
        assert t608001110_x210(z4=89000020, z5=1047600368, z6=1)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 537:
        """State 150"""
        assert t608001110_x210(z4=89000021, z5=1047600368, z6=0)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 138:
        """State 152"""
        assert t608001110_x210(z4=89000020, z5=1047600370, z6=1)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 538:
        """State 154"""
        assert t608001110_x210(z4=89000021, z5=1047600370, z6=0)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 139:
        """State 156"""
        assert t608001110_x210(z4=89000020, z5=1047600050, z6=1)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 539:
        """State 158"""
        assert t608001110_x210(z4=89000021, z5=1047600050, z6=0)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 140:
        """State 160"""
        assert t608001110_x210(z4=89000020, z5=1047600052, z6=1)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 540:
        """State 162"""
        assert t608001110_x210(z4=89000021, z5=1047600052, z6=0)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 141:
        """State 164"""
        assert t608001110_x210(z4=89000020, z5=1047600364, z6=1)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 541:
        """State 166"""
        assert t608001110_x210(z4=89000021, z5=1047600364, z6=0)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 142:
        """State 168"""
        assert t608001110_x210(z4=89000020, z5=1047600366, z6=1)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 542:
        """State 170"""
        assert t608001110_x210(z4=89000021, z5=1047600366, z6=0)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 143:
        """State 172"""
        assert t608001110_x210(z4=89000020, z5=1047600376, z6=1)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 543:
        """State 174"""
        assert t608001110_x210(z4=89000021, z5=1047600376, z6=0)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 144:
        """State 176"""
        assert t608001110_x210(z4=89000020, z5=1047600378, z6=1)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 544:
        """State 178"""
        assert t608001110_x210(z4=89000021, z5=1047600378, z6=0)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 145:
        """State 180"""
        assert t608001110_x210(z4=89000020, z5=1047600360, z6=1)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 545:
        """State 182"""
        assert t608001110_x210(z4=89000021, z5=1047600360, z6=0)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 146:
        """State 184"""
        assert t608001110_x210(z4=89000020, z5=1047600362, z6=1)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 546:
        """State 186"""
        assert t608001110_x210(z4=89000021, z5=1047600362, z6=0)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 147:
        """State 188"""
        assert t608001110_x210(z4=89000020, z5=1047600372, z6=1)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 547:
        """State 190"""
        assert t608001110_x210(z4=89000021, z5=1047600372, z6=0)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 148:
        """State 192"""
        assert t608001110_x210(z4=89000020, z5=1047600374, z6=1)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 548:
        """State 194"""
        assert t608001110_x210(z4=89000021, z5=1047600374, z6=0)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 149:
        """State 196"""
        assert t608001110_x210(z4=89000020, z5=1047600384, z6=1)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 549:
        """State 198"""
        assert t608001110_x210(z4=89000021, z5=1047600384, z6=0)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 150:
        """State 200"""
        assert t608001110_x210(z4=89000020, z5=1047600386, z6=1)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 550:
        """State 202"""
        assert t608001110_x210(z4=89000021, z5=1047600386, z6=0)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 151:
        """State 204"""
        assert t608001110_x210(z4=89000020, z5=1047600110, z6=1)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 551:
        """State 206"""
        assert t608001110_x210(z4=89000021, z5=1047600110, z6=0)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 152:
        """State 208"""
        assert t608001110_x210(z4=89000020, z5=1047600108, z6=1)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 552:
        """State 210"""
        assert t608001110_x210(z4=89000021, z5=1047600108, z6=0)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 153:
        """State 212"""
        assert t608001110_x210(z4=89000020, z5=1047600430, z6=1)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 553:
        """State 214"""
        assert t608001110_x210(z4=89000021, z5=1047600430, z6=0)
        """State 215"""
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x62():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600155), 101, 89001300, -1)
    AddTalkListDataIf(GetEventFlag(1047600155) == 1, 501, 89001300, -1)
    AddTalkListDataIf(not GetEventFlag(1047600157), 102, 89001301, -1)
    AddTalkListDataIf(GetEventFlag(1047600157) == 1, 502, 89001301, -1)
    AddTalkListDataIf(not GetEventFlag(1047600196), 103, 89001302, -1)
    AddTalkListDataIf(GetEventFlag(1047600196) == 1, 503, 89001302, -1)
    AddTalkListDataIf(not GetEventFlag(1047600224), 104, 89001303, -1)
    AddTalkListDataIf(GetEventFlag(1047600224) == 1, 504, 89001303, -1)
    AddTalkListDataIf(not GetEventFlag(1047600226), 105, 89001304, -1)
    AddTalkListDataIf(GetEventFlag(1047600226) == 1, 505, 89001304, -1)
    AddTalkListDataIf(not GetEventFlag(1047600345), 106, 89001305, -1)
    AddTalkListDataIf(GetEventFlag(1047600345) == 1, 506, 89001305, -1)
    AddTalkListDataIf(not GetEventFlag(1047600286), 107, 89001306, -1)
    AddTalkListDataIf(GetEventFlag(1047600286) == 1, 507, 89001306, -1)
    AddTalkListDataIf(not GetEventFlag(1047600288), 108, 89001307, -1)
    AddTalkListDataIf(GetEventFlag(1047600288) == 1, 508, 89001307, -1)
    AddTalkListDataIf(not GetEventFlag(1047600302), 109, 89001308, -1)
    AddTalkListDataIf(GetEventFlag(1047600302) == 1, 509, 89001308, -1)
    AddTalkListDataIf(not GetEventFlag(1047600304), 110, 89001309, -1)
    AddTalkListDataIf(GetEventFlag(1047600304) == 1, 510, 89001309, -1)
    AddTalkListDataIf(not GetEventFlag(1047600348), 111, 89001310, -1)
    AddTalkListDataIf(GetEventFlag(1047600348) == 1, 511, 89001310, -1)
    AddTalkListDataIf(not GetEventFlag(1047600350), 112, 89001311, -1)
    AddTalkListDataIf(GetEventFlag(1047600350) == 1, 512, 89001311, -1)
    AddTalkListDataIf(not GetEventFlag(1047600352), 113, 89001312, -1)
    AddTalkListDataIf(GetEventFlag(1047600352) == 1, 513, 89001312, -1)
    AddTalkListDataIf(not GetEventFlag(1047600354), 114, 89001313, -1)
    AddTalkListDataIf(GetEventFlag(1047600354) == 1, 514, 89001313, -1)
    AddTalkListDataIf(not GetEventFlag(1047600358), 115, 89001314, -1)
    AddTalkListDataIf(GetEventFlag(1047600358) == 1, 515, 89001314, -1)
    AddTalkListDataIf(not GetEventFlag(1047600250), 116, 89001315, -1)
    AddTalkListDataIf(GetEventFlag(1047600250) == 1, 516, 89001315, -1)
    AddTalkListDataIf(not GetEventFlag(1047600252), 117, 89001316, -1)
    AddTalkListDataIf(GetEventFlag(1047600252) == 1, 517, 89001316, -1)
    AddTalkListDataIf(not GetEventFlag(1047600186), 118, 89001317, -1)
    AddTalkListDataIf(GetEventFlag(1047600186) == 1, 518, 89001317, -1)
    AddTalkListDataIf(not GetEventFlag(1047600188), 119, 89001318, -1)
    AddTalkListDataIf(GetEventFlag(1047600188) == 1, 519, 89001318, -1)
    AddTalkListDataIf(not GetEventFlag(1047600380), 120, 89001319, -1)
    AddTalkListDataIf(GetEventFlag(1047600380) == 1, 520, 89001319, -1)
    AddTalkListDataIf(not GetEventFlag(1047600382), 121, 89001320, -1)
    AddTalkListDataIf(GetEventFlag(1047600382) == 1, 521, 89001320, -1)
    AddTalkListDataIf(not GetEventFlag(1047600282), 122, 89001321, -1)
    AddTalkListDataIf(GetEventFlag(1047600282) == 1, 522, 89001321, -1)
    AddTalkListDataIf(not GetEventFlag(1047600284), 123, 89001322, -1)
    AddTalkListDataIf(GetEventFlag(1047600284) == 1, 523, 89001322, -1)
    AddTalkListDataIf(not GetEventFlag(1047600004), 124, 89001323, -1)
    AddTalkListDataIf(GetEventFlag(1047600004) == 1, 524, 89001323, -1)
    AddTalkListDataIf(not GetEventFlag(1047600006), 125, 89001324, -1)
    AddTalkListDataIf(GetEventFlag(1047600006) == 1, 525, 89001324, -1)
    AddTalkListDataIf(not GetEventFlag(1047600040), 126, 89001325, -1)
    AddTalkListDataIf(GetEventFlag(1047600040) == 1, 526, 89001325, -1)
    AddTalkListDataIf(not GetEventFlag(1047600042), 127, 89001326, -1)
    AddTalkListDataIf(GetEventFlag(1047600042) == 1, 527, 89001326, -1)
    AddTalkListDataIf(not GetEventFlag(1047600044), 128, 89001327, -1)
    AddTalkListDataIf(GetEventFlag(1047600044) == 1, 528, 89001327, -1)
    AddTalkListDataIf(not GetEventFlag(1047600127), 129, 89001328, -1)
    AddTalkListDataIf(GetEventFlag(1047600127) == 1, 529, 89001328, -1)
    AddTalkListDataIf(not GetEventFlag(1047600129), 130, 89001329, -1)
    AddTalkListDataIf(GetEventFlag(1047600129) == 1, 530, 89001329, -1)
    AddTalkListDataIf(not GetEventFlag(1047600030), 131, 89001330, -1)
    AddTalkListDataIf(GetEventFlag(1047600030) == 1, 531, 89001330, -1)
    AddTalkListDataIf(not GetEventFlag(1047600032), 132, 89001331, -1)
    AddTalkListDataIf(GetEventFlag(1047600032) == 1, 532, 89001331, -1)
    AddTalkListDataIf(not GetEventFlag(1047600331), 133, 89001332, -1)
    AddTalkListDataIf(GetEventFlag(1047600331) == 1, 533, 89001332, -1)
    AddTalkListDataIf(not GetEventFlag(1047600000), 134, 89001333, -1)
    AddTalkListDataIf(GetEventFlag(1047600000) == 1, 534, 89001333, -1)
    AddTalkListDataIf(not GetEventFlag(1047600002), 135, 89001334, -1)
    AddTalkListDataIf(GetEventFlag(1047600002) == 1, 535, 89001334, -1)
    AddTalkListDataIf(not GetEventFlag(1047600356), 136, 89001335, -1)
    AddTalkListDataIf(GetEventFlag(1047600356) == 1, 536, 89001335, -1)
    AddTalkListDataIf(not GetEventFlag(1047600062), 137, 89001336, -1)
    AddTalkListDataIf(GetEventFlag(1047600062) == 1, 537, 89001336, -1)
    AddTalkListDataIf(not GetEventFlag(1047600064), 138, 89001337, -1)
    AddTalkListDataIf(GetEventFlag(1047600064) == 1, 538, 89001337, -1)
    AddTalkListDataIf(not GetEventFlag(1047600322), 139, 89001338, -1)
    AddTalkListDataIf(GetEventFlag(1047600322) == 1, 539, 89001338, -1)
    AddTalkListDataIf(not GetEventFlag(1047600216), 140, 89001339, -1)
    AddTalkListDataIf(GetEventFlag(1047600216) == 1, 540, 89001339, -1)
    AddTalkListDataIf(not GetEventFlag(1047600218), 141, 89001340, -1)
    AddTalkListDataIf(GetEventFlag(1047600218) == 1, 541, 89001340, -1)
    AddTalkListDataIf(not GetEventFlag(1047600100), 142, 89001341, -1)
    AddTalkListDataIf(GetEventFlag(1047600100) == 1, 542, 89001341, -1)
    AddTalkListDataIf(not GetEventFlag(1047600102), 143, 89001342, -1)
    AddTalkListDataIf(GetEventFlag(1047600102) == 1, 543, 89001342, -1)
    AddTalkListDataIf(not GetEventFlag(1047600094), 144, 89001343, -1)
    AddTalkListDataIf(GetEventFlag(1047600094) == 1, 544, 89001343, -1)
    AddTalkListDataIf(not GetEventFlag(1047600096), 145, 89001344, -1)
    AddTalkListDataIf(GetEventFlag(1047600096) == 1, 545, 89001344, -1)
    AddTalkListDataIf(not GetEventFlag(1047600254), 146, 89001345, -1)
    AddTalkListDataIf(GetEventFlag(1047600254) == 1, 546, 89001345, -1)
    AddTalkListDataIf(not GetEventFlag(1047600256), 147, 89001346, -1)
    AddTalkListDataIf(GetEventFlag(1047600256) == 1, 547, 89001346, -1)
    AddTalkListDataIf(not GetEventFlag(1047600258), 148, 89001347, -1)
    AddTalkListDataIf(GetEventFlag(1047600258) == 1, 548, 89001347, -1)
    AddTalkListDataIf(not GetEventFlag(1047600388), 149, 89001348, -1)
    AddTalkListDataIf(GetEventFlag(1047600388) == 1, 549, 89001348, -1)
    AddTalkListDataIf(not GetEventFlag(1047600390), 150, 89001349, -1)
    AddTalkListDataIf(GetEventFlag(1047600390) == 1, 550, 89001349, -1)
    AddTalkListDataIf(not GetEventFlag(1047600392), 151, 89001350, -1)
    AddTalkListDataIf(GetEventFlag(1047600392) == 1, 551, 89001350, -1)
    AddTalkListDataIf(not GetEventFlag(1047600394), 152, 89001351, -1)
    AddTalkListDataIf(GetEventFlag(1047600394) == 1, 552, 89001351, -1)
    AddTalkListDataIf(not GetEventFlag(1047600396), 153, 89001352, -1)
    AddTalkListDataIf(GetEventFlag(1047600396) == 1, 553, 89001352, -1)
    AddTalkListDataIf(not GetEventFlag(1047600084), 154, 89001353, -1)
    AddTalkListDataIf(GetEventFlag(1047600084) == 1, 554, 89001353, -1)
    AddTalkListDataIf(not GetEventFlag(1047600086), 155, 89001354, -1)
    AddTalkListDataIf(GetEventFlag(1047600086) == 1, 555, 89001354, -1)
    AddTalkListDataIf(not GetEventFlag(1047600088), 156, 89001355, -1)
    AddTalkListDataIf(GetEventFlag(1047600088) == 1, 556, 89001355, -1)
    AddTalkListDataIf(not GetEventFlag(1047600260), 157, 89001356, -1)
    AddTalkListDataIf(GetEventFlag(1047600260) == 1, 557, 89001356, -1)
    AddTalkListDataIf(not GetEventFlag(1047600262), 158, 89001357, -1)
    AddTalkListDataIf(GetEventFlag(1047600262) == 1, 558, 89001357, -1)
    AddTalkListDataIf(not GetEventFlag(1047600080), 159, 89001358, -1)
    AddTalkListDataIf(GetEventFlag(1047600080) == 1, 559, 89001358, -1)
    AddTalkListDataIf(not GetEventFlag(1047600082), 160, 89001359, -1)
    AddTalkListDataIf(GetEventFlag(1047600082) == 1, 560, 89001359, -1)
    AddTalkListDataIf(not GetEventFlag(1047600122), 161, 89001360, -1)
    AddTalkListDataIf(GetEventFlag(1047600122) == 1, 561, 89001360, -1)
    AddTalkListDataIf(not GetEventFlag(1047600163), 162, 89001361, -1)
    AddTalkListDataIf(GetEventFlag(1047600163) == 1, 562, 89001361, -1)
    AddTalkListDataIf(not GetEventFlag(1047600165), 163, 89001362, -1)
    AddTalkListDataIf(GetEventFlag(1047600165) == 1, 563, 89001362, -1)
    AddTalkListDataIf(not GetEventFlag(1047600190), 164, 89001363, -1)
    AddTalkListDataIf(GetEventFlag(1047600190) == 1, 564, 89001363, -1)
    AddTalkListDataIf(not GetEventFlag(1047600398), 165, 89001364, -1)
    AddTalkListDataIf(GetEventFlag(1047600398) == 1, 565, 89001364, -1)
    AddTalkListDataIf(not GetEventFlag(1047600342), 166, 89001365, -1)
    AddTalkListDataIf(GetEventFlag(1047600342) == 1, 566, 89001365, -1)
    AddTalkListDataIf(not GetEventFlag(1047600192), 167, 89001366, -1)
    AddTalkListDataIf(GetEventFlag(1047600192) == 1, 567, 89001366, -1)
    AddTalkListDataIf(not GetEventFlag(1047600194), 168, 89001367, -1)
    AddTalkListDataIf(GetEventFlag(1047600194) == 1, 568, 89001367, -1)
    AddTalkListDataIf(not GetEventFlag(1047600280), 169, 89001368, -1)
    AddTalkListDataIf(GetEventFlag(1047600280) == 1, 569, 89001368, -1)
    AddTalkListDataIf(not GetEventFlag(1047600275), 170, 89001369, -1)
    AddTalkListDataIf(GetEventFlag(1047600275) == 1, 570, 89001369, -1)
    AddTalkListDataIf(not GetEventFlag(1047600277), 171, 89001370, -1)
    AddTalkListDataIf(GetEventFlag(1047600277) == 1, 571, 89001370, -1)
    AddTalkListDataIf(not GetEventFlag(1047600415), 172, 89001371, -1)
    AddTalkListDataIf(GetEventFlag(1047600415) == 1, 572, 89001371, -1)
    AddTalkListDataIf(not GetEventFlag(1047600417), 173, 89001372, -1)
    AddTalkListDataIf(GetEventFlag(1047600417) == 1, 573, 89001372, -1)
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 101:
        """State 2"""
        assert t608001110_x210(z4=89000020, z5=1047600155, z6=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 4"""
        assert t608001110_x210(z4=89000021, z5=1047600155, z6=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 6"""
        assert t608001110_x210(z4=89000020, z5=1047600157, z6=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 9"""
        assert t608001110_x210(z4=89000021, z5=1047600157, z6=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 12"""
        assert t608001110_x210(z4=89000020, z5=1047600196, z6=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 14"""
        assert t608001110_x210(z4=89000021, z5=1047600196, z6=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 16"""
        assert t608001110_x210(z4=89000020, z5=1047600224, z6=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 18"""
        assert t608001110_x210(z4=89000021, z5=1047600224, z6=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 20"""
        assert t608001110_x210(z4=89000020, z5=1047600226, z6=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 22"""
        assert t608001110_x210(z4=89000021, z5=1047600226, z6=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 24"""
        assert t608001110_x210(z4=89000020, z5=1047600345, z6=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 26"""
        assert t608001110_x210(z4=89000021, z5=1047600345, z6=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 28"""
        assert t608001110_x210(z4=89000020, z5=1047600286, z6=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 30"""
        assert t608001110_x210(z4=89000021, z5=1047600286, z6=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 32"""
        assert t608001110_x210(z4=89000020, z5=1047600288, z6=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 34"""
        assert t608001110_x210(z4=89000021, z5=1047600288, z6=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 36"""
        assert t608001110_x210(z4=89000020, z5=1047600302, z6=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 509:
        """State 38"""
        assert t608001110_x210(z4=89000021, z5=1047600302, z6=0)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 40"""
        assert t608001110_x210(z4=89000020, z5=1047600304, z6=1)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 510:
        """State 42"""
        assert t608001110_x210(z4=89000021, z5=1047600304, z6=0)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 44"""
        assert t608001110_x210(z4=89000020, z5=1047600348, z6=1)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 511:
        """State 46"""
        assert t608001110_x210(z4=89000021, z5=1047600348, z6=0)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 48"""
        assert t608001110_x210(z4=89000020, z5=1047600350, z6=1)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 512:
        """State 50"""
        assert t608001110_x210(z4=89000021, z5=1047600350, z6=0)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 113:
        """State 52"""
        assert t608001110_x210(z4=89000020, z5=1047600352, z6=1)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 513:
        """State 54"""
        assert t608001110_x210(z4=89000021, z5=1047600352, z6=0)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 114:
        """State 56"""
        assert t608001110_x210(z4=89000020, z5=1047600354, z6=1)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 514:
        """State 58"""
        assert t608001110_x210(z4=89000021, z5=1047600354, z6=0)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 115:
        """State 60"""
        assert t608001110_x210(z4=89000020, z5=1047600358, z6=1)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 515:
        """State 62"""
        assert t608001110_x210(z4=89000021, z5=1047600358, z6=0)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 116:
        """State 64"""
        assert t608001110_x210(z4=89000020, z5=1047600250, z6=1)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 516:
        """State 66"""
        assert t608001110_x210(z4=89000021, z5=1047600250, z6=0)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 117:
        """State 68"""
        assert t608001110_x210(z4=89000020, z5=1047600252, z6=1)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 517:
        """State 70"""
        assert t608001110_x210(z4=89000021, z5=1047600252, z6=0)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 118:
        """State 72"""
        assert t608001110_x210(z4=89000020, z5=1047600186, z6=1)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 518:
        """State 74"""
        assert t608001110_x210(z4=89000021, z5=1047600186, z6=0)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 119:
        """State 76"""
        assert t608001110_x210(z4=89000020, z5=1047600188, z6=1)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 519:
        """State 78"""
        assert t608001110_x210(z4=89000021, z5=1047600188, z6=0)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 120:
        """State 80"""
        assert t608001110_x210(z4=89000020, z5=1047600380, z6=1)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 520:
        """State 82"""
        assert t608001110_x210(z4=89000021, z5=1047600380, z6=0)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 121:
        """State 84"""
        assert t608001110_x210(z4=89000020, z5=1047600382, z6=1)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 521:
        """State 86"""
        assert t608001110_x210(z4=89000021, z5=1047600382, z6=0)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 122:
        """State 88"""
        assert t608001110_x210(z4=89000020, z5=1047600282, z6=1)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 522:
        """State 90"""
        assert t608001110_x210(z4=89000021, z5=1047600282, z6=0)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 123:
        """State 92"""
        assert t608001110_x210(z4=89000020, z5=1047600284, z6=1)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 523:
        """State 94"""
        assert t608001110_x210(z4=89000021, z5=1047600284, z6=0)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 124:
        """State 96"""
        assert t608001110_x210(z4=89000020, z5=1047600004, z6=1)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 524:
        """State 98"""
        assert t608001110_x210(z4=89000021, z5=1047600004, z6=0)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 125:
        """State 100"""
        assert t608001110_x210(z4=89000020, z5=1047600006, z6=1)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 525:
        """State 102"""
        assert t608001110_x210(z4=89000021, z5=1047600006, z6=0)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 126:
        """State 104"""
        assert t608001110_x210(z4=89000020, z5=1047600040, z6=1)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 526:
        """State 106"""
        assert t608001110_x210(z4=89000021, z5=1047600040, z6=0)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 127:
        """State 108"""
        assert t608001110_x210(z4=89000020, z5=1047600042, z6=1)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 527:
        """State 110"""
        assert t608001110_x210(z4=89000021, z5=1047600042, z6=0)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 128:
        """State 112"""
        assert t608001110_x210(z4=89000020, z5=1047600044, z6=1)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 528:
        """State 114"""
        assert t608001110_x210(z4=89000021, z5=1047600044, z6=0)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 129:
        """State 116"""
        assert t608001110_x210(z4=89000020, z5=1047600127, z6=1)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 529:
        """State 118"""
        assert t608001110_x210(z4=89000021, z5=1047600127, z6=0)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 130:
        """State 120"""
        assert t608001110_x210(z4=89000020, z5=1047600129, z6=1)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 530:
        """State 122"""
        assert t608001110_x210(z4=89000021, z5=1047600129, z6=0)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 131:
        """State 124"""
        assert t608001110_x210(z4=89000020, z5=1047600030, z6=1)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 531:
        """State 126"""
        assert t608001110_x210(z4=89000021, z5=1047600030, z6=0)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 132:
        """State 128"""
        assert t608001110_x210(z4=89000020, z5=1047600032, z6=1)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 532:
        """State 130"""
        assert t608001110_x210(z4=89000021, z5=1047600032, z6=0)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 133:
        """State 132"""
        assert t608001110_x210(z4=89000020, z5=1047600331, z6=1)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 533:
        """State 134"""
        assert t608001110_x210(z4=89000021, z5=1047600331, z6=0)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 134:
        """State 136"""
        assert t608001110_x210(z4=89000020, z5=1047600000, z6=1)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 534:
        """State 138"""
        assert t608001110_x210(z4=89000021, z5=1047600000, z6=0)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 135:
        """State 140"""
        assert t608001110_x210(z4=89000020, z5=1047600002, z6=1)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 535:
        """State 142"""
        assert t608001110_x210(z4=89000021, z5=1047600002, z6=0)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 136:
        """State 144"""
        assert t608001110_x210(z4=89000020, z5=1047600356, z6=1)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 536:
        """State 146"""
        assert t608001110_x210(z4=89000021, z5=1047600356, z6=0)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 137:
        """State 148"""
        assert t608001110_x210(z4=89000020, z5=1047600062, z6=1)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 537:
        """State 150"""
        assert t608001110_x210(z4=89000021, z5=1047600062, z6=0)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 138:
        """State 152"""
        assert t608001110_x210(z4=89000020, z5=1047600064, z6=1)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 538:
        """State 154"""
        assert t608001110_x210(z4=89000021, z5=1047600064, z6=0)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 139:
        """State 156"""
        assert t608001110_x210(z4=89000020, z5=1047600322, z6=1)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 539:
        """State 158"""
        assert t608001110_x210(z4=89000021, z5=1047600322, z6=0)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 140:
        """State 160"""
        assert t608001110_x210(z4=89000020, z5=1047600216, z6=1)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 540:
        """State 162"""
        assert t608001110_x210(z4=89000021, z5=1047600216, z6=0)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 141:
        """State 164"""
        assert t608001110_x210(z4=89000020, z5=1047600218, z6=1)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 541:
        """State 166"""
        assert t608001110_x210(z4=89000021, z5=1047600218, z6=0)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 142:
        """State 168"""
        assert t608001110_x210(z4=89000020, z5=1047600100, z6=1)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 542:
        """State 170"""
        assert t608001110_x210(z4=89000021, z5=1047600100, z6=0)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 143:
        """State 172"""
        assert t608001110_x210(z4=89000020, z5=1047600102, z6=1)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 543:
        """State 174"""
        assert t608001110_x210(z4=89000021, z5=1047600102, z6=0)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 144:
        """State 176"""
        assert t608001110_x210(z4=89000020, z5=1047600094, z6=1)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 544:
        """State 178"""
        assert t608001110_x210(z4=89000021, z5=1047600094, z6=0)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 145:
        """State 180"""
        assert t608001110_x210(z4=89000020, z5=1047600096, z6=1)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 545:
        """State 182"""
        assert t608001110_x210(z4=89000021, z5=1047600096, z6=0)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 146:
        """State 184"""
        assert t608001110_x210(z4=89000020, z5=1047600254, z6=1)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 546:
        """State 186"""
        assert t608001110_x210(z4=89000021, z5=1047600254, z6=0)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 147:
        """State 188"""
        assert t608001110_x210(z4=89000020, z5=1047600256, z6=1)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 547:
        """State 190"""
        assert t608001110_x210(z4=89000021, z5=1047600256, z6=0)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 148:
        """State 192"""
        assert t608001110_x210(z4=89000020, z5=1047600258, z6=1)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 548:
        """State 194"""
        assert t608001110_x210(z4=89000021, z5=1047600258, z6=0)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 149:
        """State 196"""
        assert t608001110_x210(z4=89000020, z5=1047600388, z6=1)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 549:
        """State 198"""
        assert t608001110_x210(z4=89000021, z5=1047600388, z6=0)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 150:
        """State 200"""
        assert t608001110_x210(z4=89000020, z5=1047600390, z6=1)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 550:
        """State 202"""
        assert t608001110_x210(z4=89000021, z5=1047600390, z6=0)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 151:
        """State 204"""
        assert t608001110_x210(z4=89000020, z5=1047600392, z6=1)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 551:
        """State 206"""
        assert t608001110_x210(z4=89000021, z5=1047600392, z6=0)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 152:
        """State 208"""
        assert t608001110_x210(z4=89000020, z5=1047600394, z6=1)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 552:
        """State 210"""
        assert t608001110_x210(z4=89000021, z5=1047600394, z6=0)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 153:
        """State 212"""
        assert t608001110_x210(z4=89000020, z5=1047600396, z6=1)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 553:
        """State 214"""
        assert t608001110_x210(z4=89000021, z5=1047600396, z6=0)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 154:
        """State 216"""
        assert t608001110_x210(z4=89000020, z5=1047600084, z6=1)
        """State 217"""
        return 0
    elif GetTalkListEntryResult() == 554:
        """State 218"""
        assert t608001110_x210(z4=89000021, z5=1047600084, z6=0)
        """State 219"""
        return 0
    elif GetTalkListEntryResult() == 155:
        """State 220"""
        assert t608001110_x210(z4=89000020, z5=1047600086, z6=1)
        """State 221"""
        return 0
    elif GetTalkListEntryResult() == 555:
        """State 222"""
        assert t608001110_x210(z4=89000021, z5=1047600086, z6=0)
        """State 223"""
        return 0
    elif GetTalkListEntryResult() == 156:
        """State 224"""
        assert t608001110_x210(z4=89000020, z5=1047600088, z6=1)
        """State 225"""
        return 0
    elif GetTalkListEntryResult() == 556:
        """State 226"""
        assert t608001110_x210(z4=89000021, z5=1047600088, z6=0)
        """State 227"""
        return 0
    elif GetTalkListEntryResult() == 157:
        """State 228"""
        assert t608001110_x210(z4=89000020, z5=1047600260, z6=1)
        """State 229"""
        return 0
    elif GetTalkListEntryResult() == 557:
        """State 230"""
        assert t608001110_x210(z4=89000021, z5=1047600260, z6=0)
        """State 231"""
        return 0
    elif GetTalkListEntryResult() == 158:
        """State 232"""
        assert t608001110_x210(z4=89000020, z5=1047600262, z6=1)
        """State 233"""
        return 0
    elif GetTalkListEntryResult() == 558:
        """State 234"""
        assert t608001110_x210(z4=89000021, z5=1047600262, z6=0)
        """State 235"""
        return 0
    elif GetTalkListEntryResult() == 159:
        """State 236"""
        assert t608001110_x210(z4=89000020, z5=1047600080, z6=1)
        """State 237"""
        return 0
    elif GetTalkListEntryResult() == 559:
        """State 238"""
        assert t608001110_x210(z4=89000021, z5=1047600080, z6=0)
        """State 239"""
        return 0
    elif GetTalkListEntryResult() == 160:
        """State 240"""
        assert t608001110_x210(z4=89000020, z5=1047600082, z6=1)
        """State 241"""
        return 0
    elif GetTalkListEntryResult() == 560:
        """State 242"""
        assert t608001110_x210(z4=89000021, z5=1047600082, z6=0)
        """State 243"""
        return 0
    elif GetTalkListEntryResult() == 161:
        """State 244"""
        assert t608001110_x210(z4=89000020, z5=1047600122, z6=1)
        """State 245"""
        return 0
    elif GetTalkListEntryResult() == 561:
        """State 246"""
        assert t608001110_x210(z4=89000021, z5=1047600122, z6=0)
        """State 247"""
        return 0
    elif GetTalkListEntryResult() == 162:
        """State 248"""
        assert t608001110_x210(z4=89000020, z5=1047600163, z6=1)
        """State 249"""
        return 0
    elif GetTalkListEntryResult() == 562:
        """State 250"""
        assert t608001110_x210(z4=89000021, z5=1047600163, z6=0)
        """State 251"""
        return 0
    elif GetTalkListEntryResult() == 163:
        """State 252"""
        assert t608001110_x210(z4=89000020, z5=1047600165, z6=1)
        """State 253"""
        return 0
    elif GetTalkListEntryResult() == 563:
        """State 254"""
        assert t608001110_x210(z4=89000021, z5=1047600165, z6=0)
        """State 255"""
        return 0
    elif GetTalkListEntryResult() == 164:
        """State 256"""
        assert t608001110_x210(z4=89000020, z5=1047600190, z6=1)
        """State 257"""
        return 0
    elif GetTalkListEntryResult() == 564:
        """State 258"""
        assert t608001110_x210(z4=89000021, z5=1047600190, z6=0)
        """State 259"""
        return 0
    elif GetTalkListEntryResult() == 165:
        """State 260"""
        assert t608001110_x210(z4=89000020, z5=1047600398, z6=1)
        """State 261"""
        return 0
    elif GetTalkListEntryResult() == 565:
        """State 262"""
        assert t608001110_x210(z4=89000021, z5=1047600398, z6=0)
        """State 263"""
        return 0
    elif GetTalkListEntryResult() == 166:
        """State 264"""
        assert t608001110_x210(z4=89000020, z5=1047600342, z6=1)
        """State 265"""
        return 0
    elif GetTalkListEntryResult() == 566:
        """State 266"""
        assert t608001110_x210(z4=89000021, z5=1047600342, z6=0)
        """State 267"""
        return 0
    elif GetTalkListEntryResult() == 167:
        """State 268"""
        assert t608001110_x210(z4=89000020, z5=1047600192, z6=1)
        """State 269"""
        return 0
    elif GetTalkListEntryResult() == 567:
        """State 270"""
        assert t608001110_x210(z4=89000021, z5=1047600192, z6=0)
        """State 271"""
        return 0
    elif GetTalkListEntryResult() == 168:
        """State 272"""
        assert t608001110_x210(z4=89000020, z5=1047600194, z6=1)
        """State 273"""
        return 0
    elif GetTalkListEntryResult() == 568:
        """State 274"""
        assert t608001110_x210(z4=89000021, z5=1047600194, z6=0)
        """State 275"""
        return 0
    elif GetTalkListEntryResult() == 169:
        """State 276"""
        assert t608001110_x210(z4=89000020, z5=1047600280, z6=1)
        """State 277"""
        return 0
    elif GetTalkListEntryResult() == 569:
        """State 278"""
        assert t608001110_x210(z4=89000021, z5=1047600280, z6=0)
        """State 279"""
        return 0
    elif GetTalkListEntryResult() == 170:
        """State 280"""
        assert t608001110_x210(z4=89000020, z5=1047600275, z6=1)
        """State 281"""
        return 0
    elif GetTalkListEntryResult() == 570:
        """State 282"""
        assert t608001110_x210(z4=89000021, z5=1047600275, z6=0)
        """State 283"""
        return 0
    elif GetTalkListEntryResult() == 171:
        """State 284"""
        assert t608001110_x210(z4=89000020, z5=1047600277, z6=1)
        """State 285"""
        return 0
    elif GetTalkListEntryResult() == 571:
        """State 286"""
        assert t608001110_x210(z4=89000021, z5=1047600277, z6=0)
        """State 287"""
        return 0
    elif GetTalkListEntryResult() == 172:
        """State 288"""
        assert t608001110_x210(z4=89000020, z5=1047600415, z6=1)
        """State 289"""
        return 0
    elif GetTalkListEntryResult() == 572:
        """State 290"""
        assert t608001110_x210(z4=89000021, z5=1047600415, z6=0)
        """State 291"""
        return 0
    elif GetTalkListEntryResult() == 173:
        """State 292"""
        assert t608001110_x210(z4=89000020, z5=1047600417, z6=1)
        """State 293"""
        return 0
    elif GetTalkListEntryResult() == 573:
        """State 294"""
        assert t608001110_x210(z4=89000021, z5=1047600417, z6=0)
        """State 295"""
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x63():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600066), 101, 89001500, -1)
    AddTalkListDataIf(GetEventFlag(1047600066) == 1, 501, 89001500, -1)
    AddTalkListDataIf(not GetEventFlag(1047600068), 102, 89001501, -1)
    AddTalkListDataIf(GetEventFlag(1047600068) == 1, 502, 89001501, -1)
    AddTalkListDataIf(not GetEventFlag(1047600153), 103, 89001502, -1)
    AddTalkListDataIf(GetEventFlag(1047600153) == 1, 503, 89001502, -1)
    AddTalkListDataIf(not GetEventFlag(1047600151), 104, 89001503, -1)
    AddTalkListDataIf(GetEventFlag(1047600151) == 1, 504, 89001503, -1)
    AddTalkListDataIf(not GetEventFlag(1047600209), 105, 89001504, -1)
    AddTalkListDataIf(GetEventFlag(1047600209) == 1, 505, 89001504, -1)
    AddTalkListDataIf(not GetEventFlag(1047600264), 106, 89001505, -1)
    AddTalkListDataIf(GetEventFlag(1047600264) == 1, 506, 89001505, -1)
    AddTalkListDataIf(not GetEventFlag(1047600207), 107, 89001506, -1)
    AddTalkListDataIf(GetEventFlag(1047600207) == 1, 507, 89001506, -1)
    AddTalkListDataIf(not GetEventFlag(1047600409), 108, 89001507, -1)
    AddTalkListDataIf(GetEventFlag(1047600409) == 1, 508, 89001507, -1)
    AddTalkListDataIf(not GetEventFlag(1047600141), 109, 89001508, -1)
    AddTalkListDataIf(GetEventFlag(1047600141) == 1, 509, 89001508, -1)
    AddTalkListDataIf(not GetEventFlag(1047600143), 110, 89001509, -1)
    AddTalkListDataIf(GetEventFlag(1047600143) == 1, 510, 89001509, -1)
    AddTalkListDataIf(not GetEventFlag(1047600172), 111, 89001510, -1)
    AddTalkListDataIf(GetEventFlag(1047600172) == 1, 511, 89001510, -1)
    AddTalkListDataIf(not GetEventFlag(1047600174), 112, 89001511, -1)
    AddTalkListDataIf(GetEventFlag(1047600174) == 1, 512, 89001511, -1)
    AddTalkListDataIf(not GetEventFlag(1047600320), 113, 89001512, -1)
    AddTalkListDataIf(GetEventFlag(1047600320) == 1, 513, 89001512, -1)
    AddTalkListDataIf(not GetEventFlag(1047600247), 114, 89001513, -1)
    AddTalkListDataIf(GetEventFlag(1047600247) == 1, 514, 89001513, -1)
    AddTalkListDataIf(not GetEventFlag(1047600139), 115, 89001514, -1)
    AddTalkListDataIf(GetEventFlag(1047600139) == 1, 515, 89001514, -1)
    AddTalkListDataIf(not GetEventFlag(1047600338), 116, 89001515, -1)
    AddTalkListDataIf(GetEventFlag(1047600338) == 1, 516, 89001515, -1)
    AddTalkListDataIf(not GetEventFlag(1047600090), 117, 89001516, -1)
    AddTalkListDataIf(GetEventFlag(1047600090) == 1, 517, 89001516, -1)
    AddTalkListDataIf(not GetEventFlag(1047600092), 118, 89001517, -1)
    AddTalkListDataIf(GetEventFlag(1047600092) == 1, 518, 89001517, -1)
    AddTalkListDataIf(not GetEventFlag(1047600306), 119, 89001518, -1)
    AddTalkListDataIf(GetEventFlag(1047600306) == 1, 519, 89001518, -1)
    AddTalkListDataIf(not GetEventFlag(1047600308), 120, 89001519, -1)
    AddTalkListDataIf(GetEventFlag(1047600308) == 1, 520, 89001519, -1)
    AddTalkListDataIf(not GetEventFlag(1047600267), 121, 89001520, -1)
    AddTalkListDataIf(GetEventFlag(1047600267) == 1, 521, 89001520, -1)
    AddTalkListDataIf(not GetEventFlag(1047600269), 122, 89001521, -1)
    AddTalkListDataIf(GetEventFlag(1047600269) == 1, 522, 89001521, -1)
    AddTalkListDataIf(not GetEventFlag(1047600135), 123, 89001522, -1)
    AddTalkListDataIf(GetEventFlag(1047600135) == 1, 523, 89001522, -1)
    AddTalkListDataIf(not GetEventFlag(1047600271), 124, 89001523, -1)
    AddTalkListDataIf(GetEventFlag(1047600271) == 1, 524, 89001523, -1)
    AddTalkListDataIf(not GetEventFlag(1047600273), 125, 89001524, -1)
    AddTalkListDataIf(GetEventFlag(1047600273) == 1, 525, 89001524, -1)
    AddTalkListDataIf(not GetEventFlag(1047600137), 126, 89001525, -1)
    AddTalkListDataIf(GetEventFlag(1047600137) == 1, 526, 89001525, -1)
    AddTalkListDataIf(not GetEventFlag(1047600312), 127, 89001526, -1)
    AddTalkListDataIf(GetEventFlag(1047600312) == 1, 527, 89001526, -1)
    AddTalkListDataIf(not GetEventFlag(1047600314), 128, 89001527, -1)
    AddTalkListDataIf(GetEventFlag(1047600314) == 1, 528, 89001527, -1)
    AddTalkListDataIf(not GetEventFlag(1047600012), 129, 89001528, -1)
    AddTalkListDataIf(GetEventFlag(1047600012) == 1, 529, 89001528, -1)
    AddTalkListDataIf(not GetEventFlag(1047600014), 130, 89001529, -1)
    AddTalkListDataIf(GetEventFlag(1047600014) == 1, 530, 89001529, -1)
    AddTalkListDataIf(not GetEventFlag(1047600167), 131, 89001530, -1)
    AddTalkListDataIf(GetEventFlag(1047600167) == 1, 531, 89001530, -1)
    AddTalkListDataIf(not GetEventFlag(1047600169), 132, 89001531, -1)
    AddTalkListDataIf(GetEventFlag(1047600169) == 1, 532, 89001531, -1)
    AddTalkListDataIf(not GetEventFlag(1047600310), 133, 89001532, -1)
    AddTalkListDataIf(GetEventFlag(1047600310) == 1, 533, 89001532, -1)
    AddTalkListDataIf(not GetEventFlag(1047600290), 134, 89001533, -1)
    AddTalkListDataIf(GetEventFlag(1047600290) == 1, 534, 89001533, -1)
    AddTalkListDataIf(not GetEventFlag(1047600124), 135, 89001534, -1)
    AddTalkListDataIf(GetEventFlag(1047600124) == 1, 535, 89001534, -1)
    AddTalkListDataIf(not GetEventFlag(1047600318), 136, 89001535, -1)
    AddTalkListDataIf(GetEventFlag(1047600318) == 1, 536, 89001535, -1)
    AddTalkListDataIf(not GetEventFlag(1047600020), 137, 89001536, -1)
    AddTalkListDataIf(GetEventFlag(1047600020) == 1, 537, 89001536, -1)
    AddTalkListDataIf(not GetEventFlag(1047600022), 138, 89001537, -1)
    AddTalkListDataIf(GetEventFlag(1047600022) == 1, 538, 89001537, -1)
    AddTalkListDataIf(not GetEventFlag(1047600116), 139, 89001538, -1)
    AddTalkListDataIf(GetEventFlag(1047600116) == 1, 539, 89001538, -1)
    AddTalkListDataIf(not GetEventFlag(1047600118), 140, 89001539, -1)
    AddTalkListDataIf(GetEventFlag(1047600118) == 1, 540, 89001539, -1)
    AddTalkListDataIf(not GetEventFlag(1047600120), 141, 89001540, -1)
    AddTalkListDataIf(GetEventFlag(1047600120) == 1, 541, 89001540, -1)
    AddTalkListDataIf(not GetEventFlag(1047600054), 142, 89001541, -1)
    AddTalkListDataIf(GetEventFlag(1047600054) == 1, 542, 89001541, -1)
    AddTalkListDataIf(not GetEventFlag(1047600056), 143, 89001542, -1)
    AddTalkListDataIf(GetEventFlag(1047600056) == 1, 543, 89001542, -1)
    AddTalkListDataIf(not GetEventFlag(1047600098), 144, 89001543, -1)
    AddTalkListDataIf(GetEventFlag(1047600098) == 1, 544, 89001543, -1)
    AddTalkListDataIf(not GetEventFlag(1047600198), 145, 89001544, -1)
    AddTalkListDataIf(GetEventFlag(1047600198) == 1, 545, 89001544, -1)
    AddTalkListDataIf(not GetEventFlag(1047600200), 146, 89001545, -1)
    AddTalkListDataIf(GetEventFlag(1047600200) == 1, 546, 89001545, -1)
    AddTalkListDataIf(not GetEventFlag(1047600016), 147, 89001546, -1)
    AddTalkListDataIf(GetEventFlag(1047600016) == 1, 547, 89001546, -1)
    AddTalkListDataIf(not GetEventFlag(1047600018), 148, 89001547, -1)
    AddTalkListDataIf(GetEventFlag(1047600018) == 1, 548, 89001547, -1)
    AddTalkListDataIf(not GetEventFlag(1047600024), 149, 89001548, -1)
    AddTalkListDataIf(GetEventFlag(1047600024) == 1, 549, 89001548, -1)
    AddTalkListDataIf(not GetEventFlag(1047600026), 150, 89001549, -1)
    AddTalkListDataIf(GetEventFlag(1047600026) == 1, 550, 89001549, -1)
    AddTalkListDataIf(not GetEventFlag(1047600234), 151, 89001550, -1)
    AddTalkListDataIf(GetEventFlag(1047600234) == 1, 551, 89001550, -1)
    AddTalkListDataIf(not GetEventFlag(1047600236), 152, 89001551, -1)
    AddTalkListDataIf(GetEventFlag(1047600236) == 1, 552, 89001551, -1)
    AddTalkListDataIf(not GetEventFlag(1047600238), 153, 89001552, -1)
    AddTalkListDataIf(GetEventFlag(1047600238) == 1, 553, 89001552, -1)
    AddTalkListDataIf(not GetEventFlag(1047600292), 154, 89001553, -1)
    AddTalkListDataIf(GetEventFlag(1047600292) == 1, 554, 89001553, -1)
    AddTalkListDataIf(not GetEventFlag(1047600294), 155, 89001554, -1)
    AddTalkListDataIf(GetEventFlag(1047600294) == 1, 555, 89001554, -1)
    AddTalkListDataIf(not GetEventFlag(1047600405), 156, 89001555, -1)
    AddTalkListDataIf(GetEventFlag(1047600405) == 1, 556, 89001555, -1)
    AddTalkListDataIf(not GetEventFlag(1047600407), 157, 89001556, -1)
    AddTalkListDataIf(GetEventFlag(1047600407) == 1, 557, 89001556, -1)
    AddTalkListDataIf(not GetEventFlag(1047600411), 158, 89001557, -1)
    AddTalkListDataIf(GetEventFlag(1047600411) == 1, 558, 89001557, -1)
    AddTalkListDataIf(not GetEventFlag(1047600413), 159, 89001558, -1)
    AddTalkListDataIf(GetEventFlag(1047600413) == 1, 559, 89001558, -1)
    AddTalkListDataIf(not GetEventFlag(1047600034), 160, 89001559, -1)
    AddTalkListDataIf(GetEventFlag(1047600034) == 1, 560, 89001559, -1)
    AddTalkListDataIf(not GetEventFlag(1047600296), 161, 89001560, -1)
    AddTalkListDataIf(GetEventFlag(1047600296) == 1, 561, 89001560, -1)
    AddTalkListDataIf(not GetEventFlag(1047600298), 162, 89001561, -1)
    AddTalkListDataIf(GetEventFlag(1047600298) == 1, 562, 89001561, -1)
    AddTalkListDataIf(not GetEventFlag(1047600228), 163, 89001562, -1)
    AddTalkListDataIf(GetEventFlag(1047600228) == 1, 563, 89001562, -1)
    AddTalkListDataIf(not GetEventFlag(1047600230), 164, 89001563, -1)
    AddTalkListDataIf(GetEventFlag(1047600230) == 1, 564, 89001563, -1)
    AddTalkListDataIf(not GetEventFlag(1047600232), 165, 89001564, -1)
    AddTalkListDataIf(GetEventFlag(1047600232) == 1, 565, 89001564, -1)
    AddTalkListDataIf(not GetEventFlag(1047600316), 166, 89001565, -1)
    AddTalkListDataIf(GetEventFlag(1047600316) == 1, 566, 89001565, -1)
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 101:
        """State 2"""
        assert t608001110_x210(z4=89000020, z5=1047600066, z6=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 4"""
        assert t608001110_x210(z4=89000021, z5=1047600066, z6=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 6"""
        assert t608001110_x210(z4=89000020, z5=1047600068, z6=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 9"""
        assert t608001110_x210(z4=89000021, z5=1047600068, z6=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 12"""
        assert t608001110_x210(z4=89000020, z5=1047600153, z6=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 14"""
        assert t608001110_x210(z4=89000021, z5=1047600153, z6=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 16"""
        assert t608001110_x210(z4=89000020, z5=1047600151, z6=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 18"""
        assert t608001110_x210(z4=89000021, z5=1047600151, z6=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 20"""
        assert t608001110_x210(z4=89000020, z5=1047600209, z6=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 22"""
        assert t608001110_x210(z4=89000021, z5=1047600209, z6=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 24"""
        assert t608001110_x210(z4=89000020, z5=1047600264, z6=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 26"""
        assert t608001110_x210(z4=89000021, z5=1047600264, z6=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 28"""
        assert t608001110_x210(z4=89000020, z5=1047600207, z6=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 30"""
        assert t608001110_x210(z4=89000021, z5=1047600207, z6=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 32"""
        assert t608001110_x210(z4=89000020, z5=1047600409, z6=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 34"""
        assert t608001110_x210(z4=89000021, z5=1047600409, z6=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 36"""
        assert t608001110_x210(z4=89000020, z5=1047600141, z6=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 509:
        """State 38"""
        assert t608001110_x210(z4=89000021, z5=1047600141, z6=0)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 40"""
        assert t608001110_x210(z4=89000020, z5=1047600143, z6=1)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 510:
        """State 42"""
        assert t608001110_x210(z4=89000021, z5=1047600143, z6=0)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 44"""
        assert t608001110_x210(z4=89000020, z5=1047600172, z6=1)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 511:
        """State 46"""
        assert t608001110_x210(z4=89000021, z5=1047600172, z6=0)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 48"""
        assert t608001110_x210(z4=89000020, z5=1047600174, z6=1)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 512:
        """State 50"""
        assert t608001110_x210(z4=89000021, z5=1047600174, z6=0)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 113:
        """State 52"""
        assert t608001110_x210(z4=89000020, z5=1047600320, z6=1)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 513:
        """State 54"""
        assert t608001110_x210(z4=89000021, z5=1047600320, z6=0)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 114:
        """State 56"""
        assert t608001110_x210(z4=89000020, z5=1047600247, z6=1)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 514:
        """State 58"""
        assert t608001110_x210(z4=89000021, z5=1047600247, z6=0)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 115:
        """State 60"""
        assert t608001110_x210(z4=89000020, z5=1047600139, z6=1)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 515:
        """State 62"""
        assert t608001110_x210(z4=89000021, z5=1047600139, z6=0)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 116:
        """State 64"""
        assert t608001110_x210(z4=89000020, z5=1047600338, z6=1)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 516:
        """State 66"""
        assert t608001110_x210(z4=89000021, z5=1047600338, z6=0)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 117:
        """State 68"""
        assert t608001110_x210(z4=89000020, z5=1047600090, z6=1)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 517:
        """State 70"""
        assert t608001110_x210(z4=89000021, z5=1047600090, z6=0)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 118:
        """State 72"""
        assert t608001110_x210(z4=89000020, z5=1047600092, z6=1)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 518:
        """State 74"""
        assert t608001110_x210(z4=89000021, z5=1047600092, z6=0)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 119:
        """State 76"""
        assert t608001110_x210(z4=89000020, z5=1047600306, z6=1)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 519:
        """State 78"""
        assert t608001110_x210(z4=89000021, z5=1047600306, z6=0)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 120:
        """State 80"""
        assert t608001110_x210(z4=89000020, z5=1047600308, z6=1)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 520:
        """State 82"""
        assert t608001110_x210(z4=89000021, z5=1047600308, z6=0)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 121:
        """State 84"""
        assert t608001110_x210(z4=89000020, z5=1047600267, z6=1)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 521:
        """State 86"""
        assert t608001110_x210(z4=89000021, z5=1047600267, z6=0)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 122:
        """State 88"""
        assert t608001110_x210(z4=89000020, z5=1047600269, z6=1)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 522:
        """State 90"""
        assert t608001110_x210(z4=89000021, z5=1047600269, z6=0)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 123:
        """State 92"""
        assert t608001110_x210(z4=89000020, z5=1047600135, z6=1)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 523:
        """State 94"""
        assert t608001110_x210(z4=89000021, z5=1047600135, z6=0)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 124:
        """State 96"""
        assert t608001110_x210(z4=89000020, z5=1047600271, z6=1)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 524:
        """State 98"""
        assert t608001110_x210(z4=89000021, z5=1047600271, z6=0)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 125:
        """State 100"""
        assert t608001110_x210(z4=89000020, z5=1047600273, z6=1)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 525:
        """State 102"""
        assert t608001110_x210(z4=89000021, z5=1047600273, z6=0)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 126:
        """State 104"""
        assert t608001110_x210(z4=89000020, z5=1047600137, z6=1)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 526:
        """State 106"""
        assert t608001110_x210(z4=89000021, z5=1047600137, z6=0)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 127:
        """State 108"""
        assert t608001110_x210(z4=89000020, z5=1047600312, z6=1)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 527:
        """State 110"""
        assert t608001110_x210(z4=89000021, z5=1047600312, z6=0)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 128:
        """State 112"""
        assert t608001110_x210(z4=89000020, z5=1047600314, z6=1)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 528:
        """State 114"""
        assert t608001110_x210(z4=89000021, z5=1047600314, z6=0)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 129:
        """State 116"""
        assert t608001110_x210(z4=89000020, z5=1047600012, z6=1)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 529:
        """State 118"""
        assert t608001110_x210(z4=89000021, z5=1047600012, z6=0)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 130:
        """State 120"""
        assert t608001110_x210(z4=89000020, z5=1047600014, z6=1)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 530:
        """State 122"""
        assert t608001110_x210(z4=89000021, z5=1047600014, z6=0)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 131:
        """State 124"""
        assert t608001110_x210(z4=89000020, z5=1047600167, z6=1)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 531:
        """State 126"""
        assert t608001110_x210(z4=89000021, z5=1047600167, z6=0)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 132:
        """State 128"""
        assert t608001110_x210(z4=89000020, z5=1047600169, z6=1)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 532:
        """State 130"""
        assert t608001110_x210(z4=89000021, z5=1047600169, z6=0)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 133:
        """State 132"""
        assert t608001110_x210(z4=89000020, z5=1047600310, z6=1)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 533:
        """State 134"""
        assert t608001110_x210(z4=89000021, z5=1047600310, z6=0)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 134:
        """State 136"""
        assert t608001110_x210(z4=89000020, z5=1047600290, z6=1)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 534:
        """State 138"""
        assert t608001110_x210(z4=89000021, z5=1047600290, z6=0)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 135:
        """State 140"""
        assert t608001110_x210(z4=89000020, z5=1047600124, z6=1)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 535:
        """State 142"""
        assert t608001110_x210(z4=89000021, z5=1047600124, z6=0)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 136:
        """State 144"""
        assert t608001110_x210(z4=89000020, z5=1047600318, z6=1)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 536:
        """State 146"""
        assert t608001110_x210(z4=89000021, z5=1047600318, z6=0)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 137:
        """State 148"""
        assert t608001110_x210(z4=89000020, z5=1047600020, z6=1)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 537:
        """State 150"""
        assert t608001110_x210(z4=89000021, z5=1047600020, z6=0)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 138:
        """State 152"""
        assert t608001110_x210(z4=89000020, z5=1047600022, z6=1)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 538:
        """State 154"""
        assert t608001110_x210(z4=89000021, z5=1047600022, z6=0)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 139:
        """State 156"""
        assert t608001110_x210(z4=89000020, z5=1047600116, z6=1)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 539:
        """State 158"""
        assert t608001110_x210(z4=89000021, z5=1047600116, z6=0)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 140:
        """State 160"""
        assert t608001110_x210(z4=89000020, z5=1047600118, z6=1)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 540:
        """State 162"""
        assert t608001110_x210(z4=89000021, z5=1047600118, z6=0)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 141:
        """State 164"""
        assert t608001110_x210(z4=89000020, z5=1047600120, z6=1)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 541:
        """State 166"""
        assert t608001110_x210(z4=89000021, z5=1047600120, z6=0)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 142:
        """State 168"""
        assert t608001110_x210(z4=89000020, z5=1047600054, z6=1)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 542:
        """State 170"""
        assert t608001110_x210(z4=89000021, z5=1047600054, z6=0)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 143:
        """State 172"""
        assert t608001110_x210(z4=89000020, z5=1047600056, z6=1)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 543:
        """State 174"""
        assert t608001110_x210(z4=89000021, z5=1047600056, z6=0)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 144:
        """State 176"""
        assert t608001110_x210(z4=89000020, z5=1047600098, z6=1)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 544:
        """State 178"""
        assert t608001110_x210(z4=89000021, z5=1047600098, z6=0)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 145:
        """State 180"""
        assert t608001110_x210(z4=89000020, z5=1047600198, z6=1)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 545:
        """State 182"""
        assert t608001110_x210(z4=89000021, z5=1047600198, z6=0)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 146:
        """State 184"""
        assert t608001110_x210(z4=89000020, z5=1047600200, z6=1)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 546:
        """State 186"""
        assert t608001110_x210(z4=89000021, z5=1047600200, z6=0)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 147:
        """State 188"""
        assert t608001110_x210(z4=89000020, z5=1047600016, z6=1)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 547:
        """State 190"""
        assert t608001110_x210(z4=89000021, z5=1047600016, z6=0)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 148:
        """State 192"""
        assert t608001110_x210(z4=89000020, z5=1047600018, z6=1)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 548:
        """State 194"""
        assert t608001110_x210(z4=89000021, z5=1047600018, z6=0)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 149:
        """State 196"""
        assert t608001110_x210(z4=89000020, z5=1047600024, z6=1)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 549:
        """State 198"""
        assert t608001110_x210(z4=89000021, z5=1047600024, z6=0)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 150:
        """State 200"""
        assert t608001110_x210(z4=89000020, z5=1047600026, z6=1)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 550:
        """State 202"""
        assert t608001110_x210(z4=89000021, z5=1047600026, z6=0)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 151:
        """State 204"""
        assert t608001110_x210(z4=89000020, z5=1047600234, z6=1)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 551:
        """State 206"""
        assert t608001110_x210(z4=89000021, z5=1047600234, z6=0)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 152:
        """State 208"""
        assert t608001110_x210(z4=89000020, z5=1047600236, z6=1)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 552:
        """State 210"""
        assert t608001110_x210(z4=89000021, z5=1047600236, z6=0)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 153:
        """State 212"""
        assert t608001110_x210(z4=89000020, z5=1047600238, z6=1)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 553:
        """State 214"""
        assert t608001110_x210(z4=89000021, z5=1047600238, z6=0)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 154:
        """State 216"""
        assert t608001110_x210(z4=89000020, z5=1047600292, z6=1)
        """State 217"""
        return 0
    elif GetTalkListEntryResult() == 554:
        """State 218"""
        assert t608001110_x210(z4=89000021, z5=1047600292, z6=0)
        """State 219"""
        return 0
    elif GetTalkListEntryResult() == 155:
        """State 220"""
        assert t608001110_x210(z4=89000020, z5=1047600294, z6=1)
        """State 221"""
        return 0
    elif GetTalkListEntryResult() == 555:
        """State 222"""
        assert t608001110_x210(z4=89000021, z5=1047600294, z6=0)
        """State 223"""
        return 0
    elif GetTalkListEntryResult() == 156:
        """State 224"""
        assert t608001110_x210(z4=89000020, z5=1047600405, z6=1)
        """State 225"""
        return 0
    elif GetTalkListEntryResult() == 556:
        """State 226"""
        assert t608001110_x210(z4=89000021, z5=1047600405, z6=0)
        """State 227"""
        return 0
    elif GetTalkListEntryResult() == 157:
        """State 228"""
        assert t608001110_x210(z4=89000020, z5=1047600407, z6=1)
        """State 229"""
        return 0
    elif GetTalkListEntryResult() == 557:
        """State 230"""
        assert t608001110_x210(z4=89000021, z5=1047600407, z6=0)
        """State 231"""
        return 0
    elif GetTalkListEntryResult() == 158:
        """State 232"""
        assert t608001110_x210(z4=89000020, z5=1047600411, z6=1)
        """State 233"""
        return 0
    elif GetTalkListEntryResult() == 558:
        """State 234"""
        assert t608001110_x210(z4=89000021, z5=1047600411, z6=0)
        """State 235"""
        return 0
    elif GetTalkListEntryResult() == 159:
        """State 236"""
        assert t608001110_x210(z4=89000020, z5=1047600413, z6=1)
        """State 237"""
        return 0
    elif GetTalkListEntryResult() == 559:
        """State 238"""
        assert t608001110_x210(z4=89000021, z5=1047600413, z6=0)
        """State 239"""
        return 0
    elif GetTalkListEntryResult() == 160:
        """State 240"""
        assert t608001110_x210(z4=89000020, z5=1047600034, z6=1)
        """State 241"""
        return 0
    elif GetTalkListEntryResult() == 560:
        """State 242"""
        assert t608001110_x210(z4=89000021, z5=1047600034, z6=0)
        """State 243"""
        return 0
    elif GetTalkListEntryResult() == 161:
        """State 244"""
        assert t608001110_x210(z4=89000020, z5=1047600296, z6=1)
        """State 245"""
        return 0
    elif GetTalkListEntryResult() == 561:
        """State 246"""
        assert t608001110_x210(z4=89000021, z5=1047600296, z6=0)
        """State 247"""
        return 0
    elif GetTalkListEntryResult() == 162:
        """State 248"""
        assert t608001110_x210(z4=89000020, z5=1047600298, z6=1)
        """State 249"""
        return 0
    elif GetTalkListEntryResult() == 562:
        """State 250"""
        assert t608001110_x210(z4=89000021, z5=1047600298, z6=0)
        """State 251"""
        return 0
    elif GetTalkListEntryResult() == 163:
        """State 252"""
        assert t608001110_x210(z4=89000020, z5=1047600228, z6=1)
        """State 253"""
        return 0
    elif GetTalkListEntryResult() == 563:
        """State 254"""
        assert t608001110_x210(z4=89000021, z5=1047600228, z6=0)
        """State 255"""
        return 0
    elif GetTalkListEntryResult() == 164:
        """State 256"""
        assert t608001110_x210(z4=89000020, z5=1047600230, z6=1)
        """State 257"""
        return 0
    elif GetTalkListEntryResult() == 564:
        """State 258"""
        assert t608001110_x210(z4=89000021, z5=1047600230, z6=0)
        """State 259"""
        return 0
    elif GetTalkListEntryResult() == 165:
        """State 260"""
        assert t608001110_x210(z4=89000020, z5=1047600232, z6=1)
        """State 261"""
        return 0
    elif GetTalkListEntryResult() == 565:
        """State 262"""
        assert t608001110_x210(z4=89000021, z5=1047600232, z6=0)
        """State 263"""
        return 0
    elif GetTalkListEntryResult() == 166:
        """State 264"""
        assert t608001110_x210(z4=89000020, z5=1047600316, z6=1)
        """State 265"""
        return 0
    elif GetTalkListEntryResult() == 566:
        """State 266"""
        assert t608001110_x210(z4=89000021, z5=1047600316, z6=0)
        """State 267"""
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x70():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600999), 100, 89001000, -1)
    AddTalkListDataIf(GetEventFlag(1047600999) == 1, 500, 89001000, -1)
    AddTalkListDataIf(not GetEventFlag(1047600421), 101, 89001800, -1)
    AddTalkListDataIf(GetEventFlag(1047600421) == 1, 501, 89001800, -1)
    AddTalkListDataIf(not GetEventFlag(1047600334), 102, 89001801, -1)
    AddTalkListDataIf(GetEventFlag(1047600334) == 1, 502, 89001801, -1)
    AddTalkListDataIf(not GetEventFlag(1047600335), 103, 89001802, -1)
    AddTalkListDataIf(GetEventFlag(1047600335) == 1, 503, 89001802, -1)
    AddTalkListDataIf(not GetEventFlag(1047600423), 104, 89001803, -1)
    AddTalkListDataIf(GetEventFlag(1047600423) == 1, 504, 89001803, -1)
    AddTalkListDataIf(not GetEventFlag(1047600424), 105, 89001804, -1)
    AddTalkListDataIf(GetEventFlag(1047600424) == 1, 505, 89001804, -1)
    AddTalkListDataIf(not GetEventFlag(1047600425), 106, 89001805, -1)
    AddTalkListDataIf(GetEventFlag(1047600425) == 1, 506, 89001805, -1)
    AddTalkListDataIf(not GetEventFlag(1047600242), 108, 89001807, -1)
    AddTalkListDataIf(GetEventFlag(1047600242) == 1, 508, 89001807, -1)
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 100:
        """State 2"""
        assert t608001110_x211(z1=89000030, z2=1047600999, z3=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 500:
        """State 4"""
        assert t608001110_x211(z1=89000031, z2=1047600999, z3=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 101:
        """State 6"""
        assert t608001110_x211(z1=89000020, z2=1047600421, z3=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 9"""
        assert t608001110_x211(z1=89000021, z2=1047600421, z3=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 12"""
        assert t608001110_x211(z1=89000020, z2=1047600334, z3=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 14"""
        assert t608001110_x211(z1=89000021, z2=1047600334, z3=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 16"""
        assert t608001110_x211(z1=89000020, z2=1047600335, z3=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 18"""
        assert t608001110_x211(z1=89000021, z2=1047600335, z3=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 20"""
        assert t608001110_x211(z1=89000020, z2=1047600423, z3=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 22"""
        assert t608001110_x211(z1=89000021, z2=1047600423, z3=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 24"""
        assert t608001110_x211(z1=89000020, z2=1047600424, z3=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 26"""
        assert t608001110_x211(z1=89000021, z2=1047600424, z3=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 28"""
        assert t608001110_x211(z1=89000020, z2=1047600425, z3=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 30"""
        assert t608001110_x211(z1=89000021, z2=1047600425, z3=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 32"""
        assert t608001110_x211(z1=89000020, z2=1047600426, z3=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 34"""
        assert t608001110_x211(z1=89000021, z2=1047600426, z3=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 36"""
        assert t608001110_x211(z1=89000020, z2=1047600242, z3=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 38"""
        assert t608001110_x211(z1=89000021, z2=1047600242, z3=0)
        """State 39"""
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x71():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600029), 101, 89001100, -1)
    AddTalkListDataIf(GetEventFlag(1047600029) == 1, 501, 89001100, -1)
    AddTalkListDataIf(not GetEventFlag(1047600113), 102, 89001101, -1)
    AddTalkListDataIf(GetEventFlag(1047600113) == 1, 502, 89001101, -1)
    AddTalkListDataIf(not GetEventFlag(1047600115), 103, 89001102, -1)
    AddTalkListDataIf(GetEventFlag(1047600115) == 1, 503, 89001102, -1)
    AddTalkListDataIf(not GetEventFlag(1047600177), 104, 89001103, -1)
    AddTalkListDataIf(GetEventFlag(1047600177) == 1, 504, 89001103, -1)
    AddTalkListDataIf(not GetEventFlag(1047600179), 105, 89001105, -1)
    AddTalkListDataIf(GetEventFlag(1047600179) == 1, 505, 89001105, -1)
    AddTalkListDataIf(not GetEventFlag(1047600301), 106, 89001104, -1)
    AddTalkListDataIf(GetEventFlag(1047600301) == 1, 506, 89001104, -1)
    AddTalkListDataIf(not GetEventFlag(1047600073), 107, 89001106, -1)
    AddTalkListDataIf(GetEventFlag(1047600073) == 1, 507, 89001106, -1)
    AddTalkListDataIf(not GetEventFlag(1047600075), 108, 89001107, -1)
    AddTalkListDataIf(GetEventFlag(1047600075) == 1, 508, 89001107, -1)
    AddTalkListDataIf(not GetEventFlag(1047600221), 109, 89001108, -1)
    AddTalkListDataIf(GetEventFlag(1047600221) == 1, 509, 89001108, -1)
    AddTalkListDataIf(not GetEventFlag(1047600223), 110, 89001109, -1)
    AddTalkListDataIf(GetEventFlag(1047600223) == 1, 510, 89001109, -1)
    AddTalkListDataIf(not GetEventFlag(1047600204), 111, 89001110, -1)
    AddTalkListDataIf(GetEventFlag(1047600204) == 1, 511, 89001110, -1)
    AddTalkListDataIf(not GetEventFlag(1047600206), 112, 89001111, -1)
    AddTalkListDataIf(GetEventFlag(1047600206) == 1, 512, 89001111, -1)
    AddTalkListDataIf(not GetEventFlag(1047600047), 113, 89001112, -1)
    AddTalkListDataIf(GetEventFlag(1047600047) == 1, 513, 89001112, -1)
    AddTalkListDataIf(not GetEventFlag(1047600049), 114, 89001113, -1)
    AddTalkListDataIf(GetEventFlag(1047600049) == 1, 514, 89001113, -1)
    AddTalkListDataIf(not GetEventFlag(1047600132), 115, 89001114, -1)
    AddTalkListDataIf(GetEventFlag(1047600132) == 1, 515, 89001114, -1)
    AddTalkListDataIf(not GetEventFlag(1047600134), 116, 89001115, -1)
    AddTalkListDataIf(GetEventFlag(1047600134) == 1, 516, 89001115, -1)
    AddTalkListDataIf(not GetEventFlag(1047600071), 117, 89001116, -1)
    AddTalkListDataIf(GetEventFlag(1047600071) == 1, 517, 89001116, -1)
    AddTalkListDataIf(not GetEventFlag(1047600009), 118, 89001117, -1)
    AddTalkListDataIf(GetEventFlag(1047600009) == 1, 518, 89001117, -1)
    AddTalkListDataIf(not GetEventFlag(1047600011), 119, 89001118, -1)
    AddTalkListDataIf(GetEventFlag(1047600011) == 1, 519, 89001118, -1)
    AddTalkListDataIf(not GetEventFlag(1047600146), 120, 89001119, -1)
    AddTalkListDataIf(GetEventFlag(1047600146) == 1, 520, 89001119, -1)
    AddTalkListDataIf(not GetEventFlag(1047600148), 121, 89001120, -1)
    AddTalkListDataIf(GetEventFlag(1047600148) == 1, 521, 89001120, -1)
    AddTalkListDataIf(not GetEventFlag(1047600150), 122, 89001121, -1)
    AddTalkListDataIf(GetEventFlag(1047600150) == 1, 522, 89001121, -1)
    AddTalkListDataIf(not GetEventFlag(1047600077), 123, 89001122, -1)
    AddTalkListDataIf(GetEventFlag(1047600077) == 1, 523, 89001122, -1)
    AddTalkListDataIf(not GetEventFlag(1047600079), 124, 89001123, -1)
    AddTalkListDataIf(GetEventFlag(1047600079) == 1, 524, 89001123, -1)
    AddTalkListDataIf(not GetEventFlag(1047600105), 125, 89001124, -1)
    AddTalkListDataIf(GetEventFlag(1047600105) == 1, 525, 89001124, -1)
    AddTalkListDataIf(not GetEventFlag(1047600107), 126, 89001125, -1)
    AddTalkListDataIf(GetEventFlag(1047600107) == 1, 526, 89001125, -1)
    AddTalkListDataIf(not GetEventFlag(1047600037), 127, 89001126, -1)
    AddTalkListDataIf(GetEventFlag(1047600037) == 1, 527, 89001126, -1)
    AddTalkListDataIf(not GetEventFlag(1047600039), 128, 89001127, -1)
    AddTalkListDataIf(GetEventFlag(1047600039) == 1, 528, 89001127, -1)
    AddTalkListDataIf(not GetEventFlag(1047600059), 129, 89001128, -1)
    AddTalkListDataIf(GetEventFlag(1047600059) == 1, 529, 89001128, -1)
    AddTalkListDataIf(not GetEventFlag(1047600061), 130, 89001129, -1)
    AddTalkListDataIf(GetEventFlag(1047600061) == 1, 530, 89001129, -1)
    AddTalkListDataIf(not GetEventFlag(1047600213), 131, 89001130, -1)
    AddTalkListDataIf(GetEventFlag(1047600213) == 1, 531, 89001130, -1)
    AddTalkListDataIf(not GetEventFlag(1047600215), 132, 89001131, -1)
    AddTalkListDataIf(GetEventFlag(1047600215) == 1, 532, 89001131, -1)
    AddTalkListDataIf(not GetEventFlag(1047600160), 133, 89001132, -1)
    AddTalkListDataIf(GetEventFlag(1047600160) == 1, 533, 89001132, -1)
    AddTalkListDataIf(not GetEventFlag(1047600162), 134, 89001133, -1)
    AddTalkListDataIf(GetEventFlag(1047600162) == 1, 534, 89001133, -1)
    AddTalkListDataIf(not GetEventFlag(1047600181), 135, 89001134, -1)
    AddTalkListDataIf(GetEventFlag(1047600181) == 1, 535, 89001134, -1)
    AddTalkListDataIf(not GetEventFlag(1047600185), 136, 89001135, -1)
    AddTalkListDataIf(GetEventFlag(1047600185) == 1, 536, 89001135, -1)
    AddTalkListDataIf(not GetEventFlag(1047600369), 137, 89001136, -1)
    AddTalkListDataIf(GetEventFlag(1047600369) == 1, 537, 89001136, -1)
    AddTalkListDataIf(not GetEventFlag(1047600371), 138, 89001137, -1)
    AddTalkListDataIf(GetEventFlag(1047600371) == 1, 538, 89001137, -1)
    AddTalkListDataIf(not GetEventFlag(1047600051), 139, 89001138, -1)
    AddTalkListDataIf(GetEventFlag(1047600051) == 1, 539, 89001138, -1)
    AddTalkListDataIf(not GetEventFlag(1047600053), 140, 89001139, -1)
    AddTalkListDataIf(GetEventFlag(1047600053) == 1, 540, 89001139, -1)
    AddTalkListDataIf(not GetEventFlag(1047600365), 141, 89001140, -1)
    AddTalkListDataIf(GetEventFlag(1047600365) == 1, 541, 89001140, -1)
    AddTalkListDataIf(not GetEventFlag(1047600367), 142, 89001141, -1)
    AddTalkListDataIf(GetEventFlag(1047600367) == 1, 542, 89001141, -1)
    AddTalkListDataIf(not GetEventFlag(1047600377), 143, 89001142, -1)
    AddTalkListDataIf(GetEventFlag(1047600377) == 1, 543, 89001142, -1)
    AddTalkListDataIf(not GetEventFlag(1047600379), 144, 89001143, -1)
    AddTalkListDataIf(GetEventFlag(1047600379) == 1, 544, 89001143, -1)
    AddTalkListDataIf(not GetEventFlag(1047600361), 145, 89001144, -1)
    AddTalkListDataIf(GetEventFlag(1047600361) == 1, 545, 89001144, -1)
    AddTalkListDataIf(not GetEventFlag(1047600363), 146, 89001145, -1)
    AddTalkListDataIf(GetEventFlag(1047600363) == 1, 546, 89001145, -1)
    AddTalkListDataIf(not GetEventFlag(1047600373), 147, 89001146, -1)
    AddTalkListDataIf(GetEventFlag(1047600373) == 1, 547, 89001146, -1)
    AddTalkListDataIf(not GetEventFlag(1047600375), 148, 89001147, -1)
    AddTalkListDataIf(GetEventFlag(1047600375) == 1, 548, 89001147, -1)
    AddTalkListDataIf(not GetEventFlag(1047600385), 149, 89001148, -1)
    AddTalkListDataIf(GetEventFlag(1047600385) == 1, 549, 89001148, -1)
    AddTalkListDataIf(not GetEventFlag(1047600387), 150, 89001149, -1)
    AddTalkListDataIf(GetEventFlag(1047600387) == 1, 550, 89001149, -1)
    AddTalkListDataIf(not GetEventFlag(1047600111), 151, 89001150, -1)
    AddTalkListDataIf(GetEventFlag(1047600111) == 1, 551, 89001150, -1)
    AddTalkListDataIf(not GetEventFlag(1047600109), 152, 89001151, -1)
    AddTalkListDataIf(GetEventFlag(1047600109) == 1, 552, 89001151, -1)
    AddTalkListDataIf(not GetEventFlag(1047600431), 153, 89001152, -1)
    AddTalkListDataIf(GetEventFlag(1047600431) == 1, 553, 89001152, -1)
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 101:
        """State 2"""
        assert t608001110_x211(z1=89000020, z2=1047600029, z3=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 4"""
        assert t608001110_x211(z1=89000021, z2=1047600029, z3=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 6"""
        assert t608001110_x211(z1=89000020, z2=1047600113, z3=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 9"""
        assert t608001110_x211(z1=89000021, z2=1047600113, z3=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 12"""
        assert t608001110_x211(z1=89000020, z2=1047600115, z3=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 14"""
        assert t608001110_x211(z1=89000021, z2=1047600115, z3=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 16"""
        assert t608001110_x211(z1=89000020, z2=1047600177, z3=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 18"""
        assert t608001110_x211(z1=89000021, z2=1047600177, z3=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 20"""
        assert t608001110_x211(z1=89000020, z2=1047600179, z3=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 22"""
        assert t608001110_x211(z1=89000021, z2=1047600179, z3=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 24"""
        assert t608001110_x211(z1=89000020, z2=1047600301, z3=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 26"""
        assert t608001110_x211(z1=89000021, z2=1047600301, z3=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 28"""
        assert t608001110_x211(z1=89000020, z2=1047600073, z3=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 30"""
        assert t608001110_x211(z1=89000021, z2=1047600073, z3=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 32"""
        assert t608001110_x211(z1=89000020, z2=1047600075, z3=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 34"""
        assert t608001110_x211(z1=89000021, z2=1047600075, z3=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 36"""
        assert t608001110_x211(z1=89000020, z2=1047600221, z3=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 509:
        """State 38"""
        assert t608001110_x211(z1=89000021, z2=1047600221, z3=0)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 40"""
        assert t608001110_x211(z1=89000020, z2=1047600223, z3=1)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 510:
        """State 42"""
        assert t608001110_x211(z1=89000021, z2=1047600223, z3=0)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 44"""
        assert t608001110_x211(z1=89000020, z2=1047600204, z3=1)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 511:
        """State 46"""
        assert t608001110_x211(z1=89000021, z2=1047600204, z3=0)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 48"""
        assert t608001110_x211(z1=89000020, z2=1047600206, z3=1)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 512:
        """State 50"""
        assert t608001110_x211(z1=89000021, z2=1047600206, z3=0)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 113:
        """State 52"""
        assert t608001110_x211(z1=89000020, z2=1047600047, z3=1)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 513:
        """State 54"""
        assert t608001110_x211(z1=89000021, z2=1047600047, z3=0)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 114:
        """State 56"""
        assert t608001110_x211(z1=89000020, z2=1047600049, z3=1)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 514:
        """State 58"""
        assert t608001110_x211(z1=89000021, z2=1047600049, z3=0)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 115:
        """State 60"""
        assert t608001110_x211(z1=89000020, z2=1047600132, z3=1)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 515:
        """State 62"""
        assert t608001110_x211(z1=89000021, z2=1047600132, z3=0)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 116:
        """State 64"""
        assert t608001110_x211(z1=89000020, z2=1047600134, z3=1)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 516:
        """State 66"""
        assert t608001110_x211(z1=89000021, z2=1047600134, z3=0)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 117:
        """State 68"""
        assert t608001110_x211(z1=89000020, z2=1047600071, z3=1)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 517:
        """State 70"""
        assert t608001110_x211(z1=89000021, z2=1047600071, z3=0)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 118:
        """State 72"""
        assert t608001110_x211(z1=89000020, z2=1047600009, z3=1)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 518:
        """State 74"""
        assert t608001110_x211(z1=89000021, z2=1047600009, z3=0)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 119:
        """State 76"""
        assert t608001110_x211(z1=89000020, z2=1047600011, z3=1)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 519:
        """State 78"""
        assert t608001110_x211(z1=89000021, z2=1047600011, z3=0)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 120:
        """State 80"""
        assert t608001110_x211(z1=89000020, z2=1047600146, z3=1)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 520:
        """State 82"""
        assert t608001110_x211(z1=89000021, z2=1047600146, z3=0)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 121:
        """State 84"""
        assert t608001110_x211(z1=89000020, z2=1047600148, z3=1)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 521:
        """State 86"""
        assert t608001110_x211(z1=89000021, z2=1047600148, z3=0)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 122:
        """State 88"""
        assert t608001110_x211(z1=89000020, z2=1047600150, z3=1)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 522:
        """State 90"""
        assert t608001110_x211(z1=89000021, z2=1047600150, z3=0)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 123:
        """State 92"""
        assert t608001110_x211(z1=89000020, z2=1047600077, z3=1)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 523:
        """State 94"""
        assert t608001110_x211(z1=89000021, z2=1047600077, z3=0)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 124:
        """State 96"""
        assert t608001110_x211(z1=89000020, z2=1047600079, z3=1)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 524:
        """State 98"""
        assert t608001110_x211(z1=89000021, z2=1047600079, z3=0)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 125:
        """State 100"""
        assert t608001110_x211(z1=89000020, z2=1047600105, z3=1)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 525:
        """State 102"""
        assert t608001110_x211(z1=89000021, z2=1047600105, z3=0)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 126:
        """State 104"""
        assert t608001110_x211(z1=89000020, z2=1047600107, z3=1)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 526:
        """State 106"""
        assert t608001110_x211(z1=89000021, z2=1047600107, z3=0)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 127:
        """State 108"""
        assert t608001110_x211(z1=89000020, z2=1047600037, z3=1)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 527:
        """State 110"""
        assert t608001110_x211(z1=89000021, z2=1047600037, z3=0)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 128:
        """State 112"""
        assert t608001110_x211(z1=89000020, z2=1047600039, z3=1)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 528:
        """State 114"""
        assert t608001110_x211(z1=89000021, z2=1047600039, z3=0)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 129:
        """State 116"""
        assert t608001110_x211(z1=89000020, z2=1047600059, z3=1)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 529:
        """State 118"""
        assert t608001110_x211(z1=89000021, z2=1047600059, z3=0)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 130:
        """State 120"""
        assert t608001110_x211(z1=89000020, z2=1047600061, z3=1)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 530:
        """State 122"""
        assert t608001110_x211(z1=89000021, z2=1047600061, z3=0)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 131:
        """State 124"""
        assert t608001110_x211(z1=89000020, z2=1047600213, z3=1)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 531:
        """State 126"""
        assert t608001110_x211(z1=89000021, z2=1047600213, z3=0)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 132:
        """State 128"""
        assert t608001110_x211(z1=89000020, z2=1047600215, z3=1)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 532:
        """State 130"""
        assert t608001110_x211(z1=89000021, z2=1047600215, z3=0)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 133:
        """State 132"""
        assert t608001110_x211(z1=89000020, z2=1047600160, z3=1)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 533:
        """State 134"""
        assert t608001110_x211(z1=89000021, z2=1047600160, z3=0)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 134:
        """State 136"""
        assert t608001110_x211(z1=89000020, z2=1047600162, z3=1)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 534:
        """State 138"""
        assert t608001110_x211(z1=89000021, z2=1047600162, z3=0)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 135:
        """State 140"""
        assert t608001110_x211(z1=89000020, z2=1047600181, z3=1)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 535:
        """State 142"""
        assert t608001110_x211(z1=89000021, z2=1047600181, z3=0)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 136:
        """State 144"""
        assert t608001110_x211(z1=89000020, z2=1047600185, z3=1)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 536:
        """State 146"""
        assert t608001110_x211(z1=89000021, z2=1047600185, z3=0)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 137:
        """State 148"""
        assert t608001110_x211(z1=89000020, z2=1047600369, z3=1)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 537:
        """State 150"""
        assert t608001110_x211(z1=89000021, z2=1047600369, z3=0)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 138:
        """State 152"""
        assert t608001110_x211(z1=89000020, z2=1047600371, z3=1)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 538:
        """State 154"""
        assert t608001110_x211(z1=89000021, z2=1047600371, z3=0)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 139:
        """State 156"""
        assert t608001110_x211(z1=89000020, z2=1047600051, z3=1)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 539:
        """State 158"""
        assert t608001110_x211(z1=89000021, z2=1047600051, z3=0)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 140:
        """State 160"""
        assert t608001110_x211(z1=89000020, z2=1047600053, z3=1)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 540:
        """State 162"""
        assert t608001110_x211(z1=89000021, z2=1047600053, z3=0)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 141:
        """State 164"""
        assert t608001110_x211(z1=89000020, z2=1047600365, z3=1)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 541:
        """State 166"""
        assert t608001110_x211(z1=89000021, z2=1047600365, z3=0)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 142:
        """State 168"""
        assert t608001110_x211(z1=89000020, z2=1047600367, z3=1)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 542:
        """State 170"""
        assert t608001110_x211(z1=89000021, z2=1047600367, z3=0)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 143:
        """State 172"""
        assert t608001110_x211(z1=89000020, z2=1047600377, z3=1)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 543:
        """State 174"""
        assert t608001110_x211(z1=89000021, z2=1047600377, z3=0)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 144:
        """State 176"""
        assert t608001110_x211(z1=89000020, z2=1047600379, z3=1)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 544:
        """State 178"""
        assert t608001110_x211(z1=89000021, z2=1047600379, z3=0)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 145:
        """State 180"""
        assert t608001110_x211(z1=89000020, z2=1047600361, z3=1)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 545:
        """State 182"""
        assert t608001110_x211(z1=89000021, z2=1047600361, z3=0)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 146:
        """State 184"""
        assert t608001110_x211(z1=89000020, z2=1047600363, z3=1)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 546:
        """State 186"""
        assert t608001110_x211(z1=89000021, z2=1047600363, z3=0)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 147:
        """State 188"""
        assert t608001110_x211(z1=89000020, z2=1047600373, z3=1)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 547:
        """State 190"""
        assert t608001110_x211(z1=89000021, z2=1047600373, z3=0)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 148:
        """State 192"""
        assert t608001110_x211(z1=89000020, z2=1047600375, z3=1)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 548:
        """State 194"""
        assert t608001110_x211(z1=89000021, z2=1047600375, z3=0)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 149:
        """State 196"""
        assert t608001110_x211(z1=89000020, z2=1047600385, z3=1)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 549:
        """State 198"""
        assert t608001110_x211(z1=89000021, z2=1047600385, z3=0)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 150:
        """State 200"""
        assert t608001110_x211(z1=89000020, z2=1047600387, z3=1)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 550:
        """State 202"""
        assert t608001110_x211(z1=89000021, z2=1047600387, z3=0)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 151:
        """State 204"""
        assert t608001110_x211(z1=89000020, z2=1047600111, z3=1)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 551:
        """State 206"""
        assert t608001110_x211(z1=89000021, z2=1047600111, z3=0)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 152:
        """State 208"""
        assert t608001110_x211(z1=89000020, z2=1047600109, z3=1)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 552:
        """State 210"""
        assert t608001110_x211(z1=89000021, z2=1047600109, z3=0)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 153:
        """State 212"""
        assert t608001110_x211(z1=89000020, z2=1047600431, z3=1)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 553:
        """State 214"""
        assert t608001110_x211(z1=89000021, z2=1047600431, z3=0)
        """State 215"""
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x72():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600156), 101, 89001300, -1)
    AddTalkListDataIf(GetEventFlag(1047600156) == 1, 501, 89001300, -1)
    AddTalkListDataIf(not GetEventFlag(1047600158), 102, 89001301, -1)
    AddTalkListDataIf(GetEventFlag(1047600158) == 1, 502, 89001301, -1)
    AddTalkListDataIf(not GetEventFlag(1047600197), 103, 89001302, -1)
    AddTalkListDataIf(GetEventFlag(1047600197) == 1, 503, 89001302, -1)
    AddTalkListDataIf(not GetEventFlag(1047600225), 104, 89001303, -1)
    AddTalkListDataIf(GetEventFlag(1047600225) == 1, 504, 89001303, -1)
    AddTalkListDataIf(not GetEventFlag(1047600227), 105, 89001304, -1)
    AddTalkListDataIf(GetEventFlag(1047600227) == 1, 505, 89001304, -1)
    AddTalkListDataIf(not GetEventFlag(1047600346), 106, 89001305, -1)
    AddTalkListDataIf(GetEventFlag(1047600346) == 1, 506, 89001305, -1)
    AddTalkListDataIf(not GetEventFlag(1047600287), 107, 89001306, -1)
    AddTalkListDataIf(GetEventFlag(1047600287) == 1, 507, 89001306, -1)
    AddTalkListDataIf(not GetEventFlag(1047600289), 108, 89001307, -1)
    AddTalkListDataIf(GetEventFlag(1047600289) == 1, 508, 89001307, -1)
    AddTalkListDataIf(not GetEventFlag(1047600303), 109, 89001308, -1)
    AddTalkListDataIf(GetEventFlag(1047600303) == 1, 509, 89001308, -1)
    AddTalkListDataIf(not GetEventFlag(1047600305), 110, 89001309, -1)
    AddTalkListDataIf(GetEventFlag(1047600305) == 1, 510, 89001309, -1)
    AddTalkListDataIf(not GetEventFlag(1047600349), 111, 89001310, -1)
    AddTalkListDataIf(GetEventFlag(1047600349) == 1, 511, 89001310, -1)
    AddTalkListDataIf(not GetEventFlag(1047600351), 112, 89001311, -1)
    AddTalkListDataIf(GetEventFlag(1047600351) == 1, 512, 89001311, -1)
    AddTalkListDataIf(not GetEventFlag(1047600353), 113, 89001312, -1)
    AddTalkListDataIf(GetEventFlag(1047600353) == 1, 513, 89001312, -1)
    AddTalkListDataIf(not GetEventFlag(1047600355), 114, 89001313, -1)
    AddTalkListDataIf(GetEventFlag(1047600355) == 1, 514, 89001313, -1)
    AddTalkListDataIf(not GetEventFlag(1047600359), 115, 89001314, -1)
    AddTalkListDataIf(GetEventFlag(1047600359) == 1, 515, 89001314, -1)
    AddTalkListDataIf(not GetEventFlag(1047600251), 116, 89001315, -1)
    AddTalkListDataIf(GetEventFlag(1047600251) == 1, 516, 89001315, -1)
    AddTalkListDataIf(not GetEventFlag(1047600253), 117, 89001316, -1)
    AddTalkListDataIf(GetEventFlag(1047600253) == 1, 517, 89001316, -1)
    AddTalkListDataIf(not GetEventFlag(1047600187), 118, 89001317, -1)
    AddTalkListDataIf(GetEventFlag(1047600187) == 1, 518, 89001317, -1)
    AddTalkListDataIf(not GetEventFlag(1047600189), 119, 89001318, -1)
    AddTalkListDataIf(GetEventFlag(1047600189) == 1, 519, 89001318, -1)
    AddTalkListDataIf(not GetEventFlag(1047600381), 120, 89001319, -1)
    AddTalkListDataIf(GetEventFlag(1047600381) == 1, 520, 89001319, -1)
    AddTalkListDataIf(not GetEventFlag(1047600383), 121, 89001320, -1)
    AddTalkListDataIf(GetEventFlag(1047600383) == 1, 521, 89001320, -1)
    AddTalkListDataIf(not GetEventFlag(1047600283), 122, 89001321, -1)
    AddTalkListDataIf(GetEventFlag(1047600283) == 1, 522, 89001321, -1)
    AddTalkListDataIf(not GetEventFlag(1047600285), 123, 89001322, -1)
    AddTalkListDataIf(GetEventFlag(1047600285) == 1, 523, 89001322, -1)
    AddTalkListDataIf(not GetEventFlag(1047600005), 124, 89001323, -1)
    AddTalkListDataIf(GetEventFlag(1047600005) == 1, 524, 89001323, -1)
    AddTalkListDataIf(not GetEventFlag(1047600007), 125, 89001324, -1)
    AddTalkListDataIf(GetEventFlag(1047600007) == 1, 525, 89001324, -1)
    AddTalkListDataIf(not GetEventFlag(1047600041), 126, 89001325, -1)
    AddTalkListDataIf(GetEventFlag(1047600041) == 1, 526, 89001325, -1)
    AddTalkListDataIf(not GetEventFlag(1047600043), 127, 89001326, -1)
    AddTalkListDataIf(GetEventFlag(1047600043) == 1, 527, 89001326, -1)
    AddTalkListDataIf(not GetEventFlag(1047600045), 128, 89001327, -1)
    AddTalkListDataIf(GetEventFlag(1047600045) == 1, 528, 89001327, -1)
    AddTalkListDataIf(not GetEventFlag(1047600128), 129, 89001328, -1)
    AddTalkListDataIf(GetEventFlag(1047600128) == 1, 529, 89001328, -1)
    AddTalkListDataIf(not GetEventFlag(1047600130), 130, 89001329, -1)
    AddTalkListDataIf(GetEventFlag(1047600130) == 1, 530, 89001329, -1)
    AddTalkListDataIf(not GetEventFlag(1047600031), 131, 89001330, -1)
    AddTalkListDataIf(GetEventFlag(1047600031) == 1, 531, 89001330, -1)
    AddTalkListDataIf(not GetEventFlag(1047600033), 132, 89001331, -1)
    AddTalkListDataIf(GetEventFlag(1047600033) == 1, 532, 89001331, -1)
    AddTalkListDataIf(not GetEventFlag(1047600332), 133, 89001332, -1)
    AddTalkListDataIf(GetEventFlag(1047600332) == 1, 533, 89001332, -1)
    AddTalkListDataIf(not GetEventFlag(1047600001), 134, 89001333, -1)
    AddTalkListDataIf(GetEventFlag(1047600001) == 1, 534, 89001333, -1)
    AddTalkListDataIf(not GetEventFlag(1047600003), 135, 89001334, -1)
    AddTalkListDataIf(GetEventFlag(1047600003) == 1, 535, 89001334, -1)
    AddTalkListDataIf(not GetEventFlag(1047600357), 136, 89001335, -1)
    AddTalkListDataIf(GetEventFlag(1047600357) == 1, 536, 89001335, -1)
    AddTalkListDataIf(not GetEventFlag(1047600063), 137, 89001336, -1)
    AddTalkListDataIf(GetEventFlag(1047600063) == 1, 537, 89001336, -1)
    AddTalkListDataIf(not GetEventFlag(1047600065), 138, 89001337, -1)
    AddTalkListDataIf(GetEventFlag(1047600065) == 1, 538, 89001337, -1)
    AddTalkListDataIf(not GetEventFlag(1047600323), 139, 89001338, -1)
    AddTalkListDataIf(GetEventFlag(1047600323) == 1, 539, 89001338, -1)
    AddTalkListDataIf(not GetEventFlag(1047600217), 140, 89001339, -1)
    AddTalkListDataIf(GetEventFlag(1047600217) == 1, 540, 89001339, -1)
    AddTalkListDataIf(not GetEventFlag(1047600219), 141, 89001340, -1)
    AddTalkListDataIf(GetEventFlag(1047600219) == 1, 541, 89001340, -1)
    AddTalkListDataIf(not GetEventFlag(1047600101), 142, 89001373, -1)
    AddTalkListDataIf(GetEventFlag(1047600101) == 1, 542, 89001373, -1)
    AddTalkListDataIf(not GetEventFlag(1047600103), 143, 89001342, -1)
    AddTalkListDataIf(GetEventFlag(1047600103) == 1, 543, 89001342, -1)
    AddTalkListDataIf(not GetEventFlag(1047600095), 144, 89001343, -1)
    AddTalkListDataIf(GetEventFlag(1047600095) == 1, 544, 89001343, -1)
    AddTalkListDataIf(not GetEventFlag(1047600097), 145, 89001344, -1)
    AddTalkListDataIf(GetEventFlag(1047600097) == 1, 545, 89001344, -1)
    AddTalkListDataIf(not GetEventFlag(1047600255), 146, 89001345, -1)
    AddTalkListDataIf(GetEventFlag(1047600255) == 1, 546, 89001345, -1)
    AddTalkListDataIf(not GetEventFlag(1047600257), 147, 89001346, -1)
    AddTalkListDataIf(GetEventFlag(1047600257) == 1, 547, 89001346, -1)
    AddTalkListDataIf(not GetEventFlag(1047600259), 148, 89001347, -1)
    AddTalkListDataIf(GetEventFlag(1047600259) == 1, 548, 89001347, -1)
    AddTalkListDataIf(not GetEventFlag(1047600389), 149, 89001348, -1)
    AddTalkListDataIf(GetEventFlag(1047600389) == 1, 549, 89001348, -1)
    AddTalkListDataIf(not GetEventFlag(1047600391), 150, 89001349, -1)
    AddTalkListDataIf(GetEventFlag(1047600391) == 1, 550, 89001349, -1)
    AddTalkListDataIf(not GetEventFlag(1047600393), 151, 89001350, -1)
    AddTalkListDataIf(GetEventFlag(1047600393) == 1, 551, 89001350, -1)
    AddTalkListDataIf(not GetEventFlag(1047600395), 152, 89001351, -1)
    AddTalkListDataIf(GetEventFlag(1047600395) == 1, 552, 89001351, -1)
    AddTalkListDataIf(not GetEventFlag(1047600397), 153, 89001352, -1)
    AddTalkListDataIf(GetEventFlag(1047600397) == 1, 553, 89001352, -1)
    AddTalkListDataIf(not GetEventFlag(1047600085), 154, 89001353, -1)
    AddTalkListDataIf(GetEventFlag(1047600085) == 1, 554, 89001353, -1)
    AddTalkListDataIf(not GetEventFlag(1047600087), 155, 89001354, -1)
    AddTalkListDataIf(GetEventFlag(1047600087) == 1, 555, 89001354, -1)
    AddTalkListDataIf(not GetEventFlag(1047600089), 156, 89001355, -1)
    AddTalkListDataIf(GetEventFlag(1047600089) == 1, 556, 89001355, -1)
    AddTalkListDataIf(not GetEventFlag(1047600261), 157, 89001356, -1)
    AddTalkListDataIf(GetEventFlag(1047600261) == 1, 557, 89001356, -1)
    AddTalkListDataIf(not GetEventFlag(1047600263), 158, 89001357, -1)
    AddTalkListDataIf(GetEventFlag(1047600263) == 1, 558, 89001357, -1)
    AddTalkListDataIf(not GetEventFlag(1047600081), 159, 89001358, -1)
    AddTalkListDataIf(GetEventFlag(1047600081) == 1, 559, 89001358, -1)
    AddTalkListDataIf(not GetEventFlag(1047600083), 160, 89001359, -1)
    AddTalkListDataIf(GetEventFlag(1047600083) == 1, 560, 89001359, -1)
    AddTalkListDataIf(not GetEventFlag(1047600123), 161, 89001360, -1)
    AddTalkListDataIf(GetEventFlag(1047600123) == 1, 561, 89001360, -1)
    AddTalkListDataIf(not GetEventFlag(1047600164), 162, 89001361, -1)
    AddTalkListDataIf(GetEventFlag(1047600164) == 1, 562, 89001361, -1)
    AddTalkListDataIf(not GetEventFlag(1047600166), 163, 89001362, -1)
    AddTalkListDataIf(GetEventFlag(1047600166) == 1, 563, 89001362, -1)
    AddTalkListDataIf(not GetEventFlag(1047600191), 164, 89001363, -1)
    AddTalkListDataIf(GetEventFlag(1047600191) == 1, 564, 89001363, -1)
    AddTalkListDataIf(not GetEventFlag(1047600399), 165, 89001364, -1)
    AddTalkListDataIf(GetEventFlag(1047600399) == 1, 565, 89001364, -1)
    AddTalkListDataIf(not GetEventFlag(1047600343), 166, 89001365, -1)
    AddTalkListDataIf(GetEventFlag(1047600343) == 1, 566, 89001365, -1)
    AddTalkListDataIf(not GetEventFlag(1047600193), 167, 89001366, -1)
    AddTalkListDataIf(GetEventFlag(1047600193) == 1, 567, 89001366, -1)
    AddTalkListDataIf(not GetEventFlag(1047600195), 168, 89001367, -1)
    AddTalkListDataIf(GetEventFlag(1047600195) == 1, 568, 89001367, -1)
    AddTalkListDataIf(not GetEventFlag(1047600281), 169, 89001368, -1)
    AddTalkListDataIf(GetEventFlag(1047600281) == 1, 569, 89001368, -1)
    AddTalkListDataIf(not GetEventFlag(1047600276), 170, 89001369, -1)
    AddTalkListDataIf(GetEventFlag(1047600276) == 1, 570, 89001369, -1)
    AddTalkListDataIf(not GetEventFlag(1047600278), 171, 89001370, -1)
    AddTalkListDataIf(GetEventFlag(1047600278) == 1, 571, 89001370, -1)
    AddTalkListDataIf(not GetEventFlag(1047600416), 172, 89001371, -1)
    AddTalkListDataIf(GetEventFlag(1047600416) == 1, 572, 89001371, -1)
    AddTalkListDataIf(not GetEventFlag(1047600418), 173, 89001372, -1)
    AddTalkListDataIf(GetEventFlag(1047600418) == 1, 573, 89001372, -1)
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 101:
        """State 2"""
        assert t608001110_x211(z1=89000020, z2=1047600156, z3=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 4"""
        assert t608001110_x211(z1=89000021, z2=1047600156, z3=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 6"""
        assert t608001110_x211(z1=89000020, z2=1047600158, z3=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 9"""
        assert t608001110_x211(z1=89000021, z2=1047600158, z3=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 12"""
        assert t608001110_x211(z1=89000020, z2=1047600197, z3=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 14"""
        assert t608001110_x211(z1=89000021, z2=1047600197, z3=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 16"""
        assert t608001110_x211(z1=89000020, z2=1047600225, z3=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 18"""
        assert t608001110_x211(z1=89000021, z2=1047600225, z3=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 20"""
        assert t608001110_x211(z1=89000020, z2=1047600227, z3=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 22"""
        assert t608001110_x211(z1=89000021, z2=1047600227, z3=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 24"""
        assert t608001110_x211(z1=89000020, z2=1047600346, z3=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 26"""
        assert t608001110_x211(z1=89000021, z2=1047600346, z3=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 28"""
        assert t608001110_x211(z1=89000020, z2=1047600287, z3=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 30"""
        assert t608001110_x211(z1=89000021, z2=1047600287, z3=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 32"""
        assert t608001110_x211(z1=89000020, z2=1047600289, z3=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 34"""
        assert t608001110_x211(z1=89000021, z2=1047600289, z3=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 36"""
        assert t608001110_x211(z1=89000020, z2=1047600303, z3=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 509:
        """State 38"""
        assert t608001110_x211(z1=89000021, z2=1047600303, z3=0)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 40"""
        assert t608001110_x211(z1=89000020, z2=1047600305, z3=1)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 510:
        """State 42"""
        assert t608001110_x211(z1=89000021, z2=1047600305, z3=0)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 44"""
        assert t608001110_x211(z1=89000020, z2=1047600349, z3=1)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 511:
        """State 46"""
        assert t608001110_x211(z1=89000021, z2=1047600349, z3=0)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 48"""
        assert t608001110_x211(z1=89000020, z2=1047600351, z3=1)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 512:
        """State 50"""
        assert t608001110_x211(z1=89000021, z2=1047600351, z3=0)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 113:
        """State 52"""
        assert t608001110_x211(z1=89000020, z2=1047600353, z3=1)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 513:
        """State 54"""
        assert t608001110_x211(z1=89000021, z2=1047600353, z3=0)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 114:
        """State 56"""
        assert t608001110_x211(z1=89000020, z2=1047600355, z3=1)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 514:
        """State 58"""
        assert t608001110_x211(z1=89000021, z2=1047600355, z3=0)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 115:
        """State 60"""
        assert t608001110_x211(z1=89000020, z2=1047600359, z3=1)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 515:
        """State 62"""
        assert t608001110_x211(z1=89000021, z2=1047600359, z3=0)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 116:
        """State 64"""
        assert t608001110_x211(z1=89000020, z2=1047600251, z3=1)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 516:
        """State 66"""
        assert t608001110_x211(z1=89000021, z2=1047600251, z3=0)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 117:
        """State 68"""
        assert t608001110_x211(z1=89000020, z2=1047600253, z3=1)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 517:
        """State 70"""
        assert t608001110_x211(z1=89000021, z2=1047600253, z3=0)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 118:
        """State 72"""
        assert t608001110_x211(z1=89000020, z2=1047600187, z3=1)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 518:
        """State 74"""
        assert t608001110_x211(z1=89000021, z2=1047600187, z3=0)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 119:
        """State 76"""
        assert t608001110_x211(z1=89000020, z2=1047600189, z3=1)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 519:
        """State 78"""
        assert t608001110_x211(z1=89000021, z2=1047600189, z3=0)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 120:
        """State 80"""
        assert t608001110_x211(z1=89000020, z2=1047600381, z3=1)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 520:
        """State 82"""
        assert t608001110_x211(z1=89000021, z2=1047600381, z3=0)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 121:
        """State 84"""
        assert t608001110_x211(z1=89000020, z2=1047600383, z3=1)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 521:
        """State 86"""
        assert t608001110_x211(z1=89000021, z2=1047600383, z3=0)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 122:
        """State 88"""
        assert t608001110_x211(z1=89000020, z2=1047600283, z3=1)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 522:
        """State 90"""
        assert t608001110_x211(z1=89000021, z2=1047600283, z3=0)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 123:
        """State 92"""
        assert t608001110_x211(z1=89000020, z2=1047600285, z3=1)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 523:
        """State 94"""
        assert t608001110_x211(z1=89000021, z2=1047600285, z3=0)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 124:
        """State 96"""
        assert t608001110_x211(z1=89000020, z2=1047600005, z3=1)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 524:
        """State 98"""
        assert t608001110_x211(z1=89000021, z2=1047600005, z3=0)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 125:
        """State 100"""
        assert t608001110_x211(z1=89000020, z2=1047600007, z3=1)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 525:
        """State 102"""
        assert t608001110_x211(z1=89000021, z2=1047600007, z3=0)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 126:
        """State 104"""
        assert t608001110_x211(z1=89000020, z2=1047600041, z3=1)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 526:
        """State 106"""
        assert t608001110_x211(z1=89000021, z2=1047600041, z3=0)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 127:
        """State 108"""
        assert t608001110_x211(z1=89000020, z2=1047600043, z3=1)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 527:
        """State 110"""
        assert t608001110_x211(z1=89000021, z2=1047600043, z3=0)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 128:
        """State 112"""
        assert t608001110_x211(z1=89000020, z2=1047600045, z3=1)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 528:
        """State 114"""
        assert t608001110_x211(z1=89000021, z2=1047600045, z3=0)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 129:
        """State 116"""
        assert t608001110_x211(z1=89000020, z2=1047600128, z3=1)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 529:
        """State 118"""
        assert t608001110_x211(z1=89000021, z2=1047600128, z3=0)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 130:
        """State 120"""
        assert t608001110_x211(z1=89000020, z2=1047600130, z3=1)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 530:
        """State 122"""
        assert t608001110_x211(z1=89000021, z2=1047600130, z3=0)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 131:
        """State 124"""
        assert t608001110_x211(z1=89000020, z2=1047600031, z3=1)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 531:
        """State 126"""
        assert t608001110_x211(z1=89000021, z2=1047600031, z3=0)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 132:
        """State 128"""
        assert t608001110_x211(z1=89000020, z2=1047600033, z3=1)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 532:
        """State 130"""
        assert t608001110_x211(z1=89000021, z2=1047600033, z3=0)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 133:
        """State 132"""
        assert t608001110_x211(z1=89000020, z2=1047600332, z3=1)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 533:
        """State 134"""
        assert t608001110_x211(z1=89000021, z2=1047600332, z3=0)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 134:
        """State 136"""
        assert t608001110_x211(z1=89000020, z2=1047600001, z3=1)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 534:
        """State 138"""
        assert t608001110_x211(z1=89000021, z2=1047600001, z3=0)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 135:
        """State 140"""
        assert t608001110_x211(z1=89000020, z2=1047600003, z3=1)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 535:
        """State 142"""
        assert t608001110_x211(z1=89000021, z2=1047600003, z3=0)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 136:
        """State 144"""
        assert t608001110_x211(z1=89000020, z2=1047600357, z3=1)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 536:
        """State 146"""
        assert t608001110_x211(z1=89000021, z2=1047600357, z3=0)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 137:
        """State 148"""
        assert t608001110_x211(z1=89000020, z2=1047600063, z3=1)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 537:
        """State 150"""
        assert t608001110_x211(z1=89000021, z2=1047600063, z3=0)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 138:
        """State 152"""
        assert t608001110_x211(z1=89000020, z2=1047600065, z3=1)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 538:
        """State 154"""
        assert t608001110_x211(z1=89000021, z2=1047600065, z3=0)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 139:
        """State 156"""
        assert t608001110_x211(z1=89000020, z2=1047600323, z3=1)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 539:
        """State 158"""
        assert t608001110_x211(z1=89000021, z2=1047600323, z3=0)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 140:
        """State 160"""
        assert t608001110_x211(z1=89000020, z2=1047600217, z3=1)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 540:
        """State 162"""
        assert t608001110_x211(z1=89000021, z2=1047600217, z3=0)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 141:
        """State 164"""
        assert t608001110_x211(z1=89000020, z2=1047600219, z3=1)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 541:
        """State 166"""
        assert t608001110_x211(z1=89000021, z2=1047600219, z3=0)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 142:
        """State 168"""
        assert t608001110_x211(z1=89000020, z2=1047600101, z3=1)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 542:
        """State 170"""
        assert t608001110_x211(z1=89000021, z2=1047600101, z3=0)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 143:
        """State 172"""
        assert t608001110_x211(z1=89000020, z2=1047600103, z3=1)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 543:
        """State 174"""
        assert t608001110_x211(z1=89000021, z2=1047600103, z3=0)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 144:
        """State 176"""
        assert t608001110_x211(z1=89000020, z2=1047600095, z3=1)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 544:
        """State 178"""
        assert t608001110_x211(z1=89000021, z2=1047600095, z3=0)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 145:
        """State 180"""
        assert t608001110_x211(z1=89000020, z2=1047600097, z3=1)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 545:
        """State 182"""
        assert t608001110_x211(z1=89000021, z2=1047600097, z3=0)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 146:
        """State 184"""
        assert t608001110_x211(z1=89000020, z2=1047600255, z3=1)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 546:
        """State 186"""
        assert t608001110_x211(z1=89000021, z2=1047600255, z3=0)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 147:
        """State 188"""
        assert t608001110_x211(z1=89000020, z2=1047600257, z3=1)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 547:
        """State 190"""
        assert t608001110_x211(z1=89000021, z2=1047600257, z3=0)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 148:
        """State 192"""
        assert t608001110_x211(z1=89000020, z2=1047600259, z3=1)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 548:
        """State 194"""
        assert t608001110_x211(z1=89000021, z2=1047600259, z3=0)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 149:
        """State 196"""
        assert t608001110_x211(z1=89000020, z2=1047600389, z3=1)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 549:
        """State 198"""
        assert t608001110_x211(z1=89000021, z2=1047600389, z3=0)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 150:
        """State 200"""
        assert t608001110_x211(z1=89000020, z2=1047600391, z3=1)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 550:
        """State 202"""
        assert t608001110_x211(z1=89000021, z2=1047600391, z3=0)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 151:
        """State 204"""
        assert t608001110_x211(z1=89000020, z2=1047600393, z3=1)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 551:
        """State 206"""
        assert t608001110_x211(z1=89000021, z2=1047600393, z3=0)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 152:
        """State 208"""
        assert t608001110_x211(z1=89000020, z2=1047600395, z3=1)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 552:
        """State 210"""
        assert t608001110_x211(z1=89000021, z2=1047600395, z3=0)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 153:
        """State 212"""
        assert t608001110_x211(z1=89000020, z2=1047600397, z3=1)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 553:
        """State 214"""
        assert t608001110_x211(z1=89000021, z2=1047600397, z3=0)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 154:
        """State 216"""
        assert t608001110_x211(z1=89000020, z2=1047600085, z3=1)
        """State 217"""
        return 0
    elif GetTalkListEntryResult() == 554:
        """State 218"""
        assert t608001110_x211(z1=89000021, z2=1047600085, z3=0)
        """State 219"""
        return 0
    elif GetTalkListEntryResult() == 155:
        """State 220"""
        assert t608001110_x211(z1=89000020, z2=1047600087, z3=1)
        """State 221"""
        return 0
    elif GetTalkListEntryResult() == 555:
        """State 222"""
        assert t608001110_x211(z1=89000021, z2=1047600087, z3=0)
        """State 223"""
        return 0
    elif GetTalkListEntryResult() == 156:
        """State 224"""
        assert t608001110_x211(z1=89000020, z2=1047600089, z3=1)
        """State 225"""
        return 0
    elif GetTalkListEntryResult() == 556:
        """State 226"""
        assert t608001110_x211(z1=89000021, z2=1047600089, z3=0)
        """State 227"""
        return 0
    elif GetTalkListEntryResult() == 157:
        """State 228"""
        assert t608001110_x211(z1=89000020, z2=1047600261, z3=1)
        """State 229"""
        return 0
    elif GetTalkListEntryResult() == 557:
        """State 230"""
        assert t608001110_x211(z1=89000021, z2=1047600261, z3=0)
        """State 231"""
        return 0
    elif GetTalkListEntryResult() == 158:
        """State 232"""
        assert t608001110_x211(z1=89000020, z2=1047600263, z3=1)
        """State 233"""
        return 0
    elif GetTalkListEntryResult() == 558:
        """State 234"""
        assert t608001110_x211(z1=89000021, z2=1047600263, z3=0)
        """State 235"""
        return 0
    elif GetTalkListEntryResult() == 159:
        """State 236"""
        assert t608001110_x211(z1=89000020, z2=1047600081, z3=1)
        """State 237"""
        return 0
    elif GetTalkListEntryResult() == 559:
        """State 238"""
        assert t608001110_x211(z1=89000021, z2=1047600081, z3=0)
        """State 239"""
        return 0
    elif GetTalkListEntryResult() == 160:
        """State 240"""
        assert t608001110_x211(z1=89000020, z2=1047600083, z3=1)
        """State 241"""
        return 0
    elif GetTalkListEntryResult() == 560:
        """State 242"""
        assert t608001110_x211(z1=89000021, z2=1047600083, z3=0)
        """State 243"""
        return 0
    elif GetTalkListEntryResult() == 161:
        """State 244"""
        assert t608001110_x211(z1=89000020, z2=1047600123, z3=1)
        """State 245"""
        return 0
    elif GetTalkListEntryResult() == 561:
        """State 246"""
        assert t608001110_x211(z1=89000021, z2=1047600123, z3=0)
        """State 247"""
        return 0
    elif GetTalkListEntryResult() == 162:
        """State 248"""
        assert t608001110_x211(z1=89000020, z2=1047600164, z3=1)
        """State 249"""
        return 0
    elif GetTalkListEntryResult() == 562:
        """State 250"""
        assert t608001110_x211(z1=89000021, z2=1047600164, z3=0)
        """State 251"""
        return 0
    elif GetTalkListEntryResult() == 163:
        """State 252"""
        assert t608001110_x211(z1=89000020, z2=1047600166, z3=1)
        """State 253"""
        return 0
    elif GetTalkListEntryResult() == 563:
        """State 254"""
        assert t608001110_x211(z1=89000021, z2=1047600166, z3=0)
        """State 255"""
        return 0
    elif GetTalkListEntryResult() == 164:
        """State 256"""
        assert t608001110_x211(z1=89000020, z2=1047600191, z3=1)
        """State 257"""
        return 0
    elif GetTalkListEntryResult() == 564:
        """State 258"""
        assert t608001110_x211(z1=89000021, z2=1047600191, z3=0)
        """State 259"""
        return 0
    elif GetTalkListEntryResult() == 165:
        """State 260"""
        assert t608001110_x211(z1=89000020, z2=1047600399, z3=1)
        """State 261"""
        return 0
    elif GetTalkListEntryResult() == 565:
        """State 262"""
        assert t608001110_x211(z1=89000021, z2=1047600399, z3=0)
        """State 263"""
        return 0
    elif GetTalkListEntryResult() == 166:
        """State 264"""
        assert t608001110_x211(z1=89000020, z2=1047600343, z3=1)
        """State 265"""
        return 0
    elif GetTalkListEntryResult() == 566:
        """State 266"""
        assert t608001110_x211(z1=89000021, z2=1047600343, z3=0)
        """State 267"""
        return 0
    elif GetTalkListEntryResult() == 167:
        """State 268"""
        assert t608001110_x211(z1=89000020, z2=1047600193, z3=1)
        """State 269"""
        return 0
    elif GetTalkListEntryResult() == 567:
        """State 270"""
        assert t608001110_x211(z1=89000021, z2=1047600193, z3=0)
        """State 271"""
        return 0
    elif GetTalkListEntryResult() == 168:
        """State 272"""
        assert t608001110_x211(z1=89000020, z2=1047600195, z3=1)
        """State 273"""
        return 0
    elif GetTalkListEntryResult() == 568:
        """State 274"""
        assert t608001110_x211(z1=89000021, z2=1047600195, z3=0)
        """State 275"""
        return 0
    elif GetTalkListEntryResult() == 169:
        """State 276"""
        assert t608001110_x211(z1=89000020, z2=1047600281, z3=1)
        """State 277"""
        return 0
    elif GetTalkListEntryResult() == 569:
        """State 278"""
        assert t608001110_x211(z1=89000021, z2=1047600281, z3=0)
        """State 279"""
        return 0
    elif GetTalkListEntryResult() == 170:
        """State 280"""
        assert t608001110_x211(z1=89000020, z2=1047600276, z3=1)
        """State 281"""
        return 0
    elif GetTalkListEntryResult() == 570:
        """State 282"""
        assert t608001110_x211(z1=89000021, z2=1047600276, z3=0)
        """State 283"""
        return 0
    elif GetTalkListEntryResult() == 171:
        """State 284"""
        assert t608001110_x211(z1=89000020, z2=1047600278, z3=1)
        """State 285"""
        return 0
    elif GetTalkListEntryResult() == 571:
        """State 286"""
        assert t608001110_x211(z1=89000021, z2=1047600278, z3=0)
        """State 287"""
        return 0
    elif GetTalkListEntryResult() == 172:
        """State 288"""
        assert t608001110_x211(z1=89000020, z2=1047600416, z3=1)
        """State 289"""
        return 0
    elif GetTalkListEntryResult() == 572:
        """State 290"""
        assert t608001110_x211(z1=89000021, z2=1047600416, z3=0)
        """State 291"""
        return 0
    elif GetTalkListEntryResult() == 173:
        """State 292"""
        assert t608001110_x211(z1=89000020, z2=1047600418, z3=1)
        """State 293"""
        return 0
    elif GetTalkListEntryResult() == 573:
        """State 294"""
        assert t608001110_x211(z1=89000021, z2=1047600418, z3=0)
        """State 295"""
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x73():
    """State 0"""
    c1_110()
    ClearTalkListData()
    AddTalkListDataIf(not GetEventFlag(1047600067), 101, 89001500, -1)
    AddTalkListDataIf(GetEventFlag(1047600067) == 1, 501, 89001500, -1)
    AddTalkListDataIf(not GetEventFlag(1047600069), 102, 89001501, -1)
    AddTalkListDataIf(GetEventFlag(1047600069) == 1, 502, 89001501, -1)
    AddTalkListDataIf(not GetEventFlag(1047600154), 103, 89001502, -1)
    AddTalkListDataIf(GetEventFlag(1047600154) == 1, 503, 89001502, -1)
    AddTalkListDataIf(not GetEventFlag(1047600152), 104, 89001503, -1)
    AddTalkListDataIf(GetEventFlag(1047600152) == 1, 504, 89001503, -1)
    AddTalkListDataIf(not GetEventFlag(1047600210), 105, 89001504, -1)
    AddTalkListDataIf(GetEventFlag(1047600210) == 1, 505, 89001504, -1)
    AddTalkListDataIf(not GetEventFlag(1047600265), 106, 89001505, -1)
    AddTalkListDataIf(GetEventFlag(1047600265) == 1, 506, 89001505, -1)
    AddTalkListDataIf(not GetEventFlag(1047600208), 107, 89001506, -1)
    AddTalkListDataIf(GetEventFlag(1047600208) == 1, 507, 89001506, -1)
    AddTalkListDataIf(not GetEventFlag(1047600410), 108, 89001507, -1)
    AddTalkListDataIf(GetEventFlag(1047600410) == 1, 508, 89001507, -1)
    AddTalkListDataIf(not GetEventFlag(1047600142), 109, 89001508, -1)
    AddTalkListDataIf(GetEventFlag(1047600142) == 1, 509, 89001508, -1)
    AddTalkListDataIf(not GetEventFlag(1047600144), 110, 89001509, -1)
    AddTalkListDataIf(GetEventFlag(1047600144) == 1, 510, 89001509, -1)
    AddTalkListDataIf(not GetEventFlag(1047600173), 111, 89001510, -1)
    AddTalkListDataIf(GetEventFlag(1047600173) == 1, 511, 89001510, -1)
    AddTalkListDataIf(not GetEventFlag(1047600175), 112, 89001511, -1)
    AddTalkListDataIf(GetEventFlag(1047600175) == 1, 512, 89001511, -1)
    AddTalkListDataIf(not GetEventFlag(1047600321), 113, 89001512, -1)
    AddTalkListDataIf(GetEventFlag(1047600321) == 1, 513, 89001512, -1)
    AddTalkListDataIf(not GetEventFlag(1047600248), 114, 89001513, -1)
    AddTalkListDataIf(GetEventFlag(1047600248) == 1, 514, 89001513, -1)
    AddTalkListDataIf(not GetEventFlag(1047600140), 115, 89001514, -1)
    AddTalkListDataIf(GetEventFlag(1047600140) == 1, 515, 89001514, -1)
    AddTalkListDataIf(not GetEventFlag(1047600339), 116, 89001515, -1)
    AddTalkListDataIf(GetEventFlag(1047600339) == 1, 516, 89001515, -1)
    AddTalkListDataIf(not GetEventFlag(1047600091), 117, 89001516, -1)
    AddTalkListDataIf(GetEventFlag(1047600091) == 1, 517, 89001516, -1)
    AddTalkListDataIf(not GetEventFlag(1047600093), 118, 89001517, -1)
    AddTalkListDataIf(GetEventFlag(1047600093) == 1, 518, 89001517, -1)
    AddTalkListDataIf(not GetEventFlag(1047600307), 119, 89001518, -1)
    AddTalkListDataIf(GetEventFlag(1047600307) == 1, 519, 89001518, -1)
    AddTalkListDataIf(not GetEventFlag(1047600309), 120, 89001519, -1)
    AddTalkListDataIf(GetEventFlag(1047600309) == 1, 520, 89001519, -1)
    AddTalkListDataIf(not GetEventFlag(1047600268), 121, 89001520, -1)
    AddTalkListDataIf(GetEventFlag(1047600268) == 1, 521, 89001520, -1)
    AddTalkListDataIf(not GetEventFlag(1047600270), 122, 89001521, -1)
    AddTalkListDataIf(GetEventFlag(1047600270) == 1, 522, 89001521, -1)
    AddTalkListDataIf(not GetEventFlag(1047600136), 123, 89001522, -1)
    AddTalkListDataIf(GetEventFlag(1047600136) == 1, 523, 89001522, -1)
    AddTalkListDataIf(not GetEventFlag(1047600272), 124, 89001523, -1)
    AddTalkListDataIf(GetEventFlag(1047600272) == 1, 524, 89001523, -1)
    AddTalkListDataIf(not GetEventFlag(1047600274), 125, 89001524, -1)
    AddTalkListDataIf(GetEventFlag(1047600274) == 1, 525, 89001524, -1)
    AddTalkListDataIf(not GetEventFlag(1047600138), 126, 89001525, -1)
    AddTalkListDataIf(GetEventFlag(1047600138) == 1, 526, 89001525, -1)
    AddTalkListDataIf(not GetEventFlag(1047600313), 127, 89001526, -1)
    AddTalkListDataIf(GetEventFlag(1047600313) == 1, 527, 89001526, -1)
    AddTalkListDataIf(not GetEventFlag(1047600315), 128, 89001527, -1)
    AddTalkListDataIf(GetEventFlag(1047600315) == 1, 528, 89001527, -1)
    AddTalkListDataIf(not GetEventFlag(1047600013), 129, 9001528, -1)
    AddTalkListDataIf(GetEventFlag(1047600013) == 1, 529, 9001528, -1)
    AddTalkListDataIf(not GetEventFlag(1047600015), 130, 89001529, -1)
    AddTalkListDataIf(GetEventFlag(1047600015) == 1, 530, 89001529, -1)
    AddTalkListDataIf(not GetEventFlag(1047600168), 131, 89001530, -1)
    AddTalkListDataIf(GetEventFlag(1047600168) == 1, 531, 89001530, -1)
    AddTalkListDataIf(not GetEventFlag(1047600170), 132, 89001531, -1)
    AddTalkListDataIf(GetEventFlag(1047600170) == 1, 532, 89001531, -1)
    AddTalkListDataIf(not GetEventFlag(1047600171), 133, 89001374, -1)
    AddTalkListDataIf(GetEventFlag(1047600171) == 1, 533, 89001374, -1)
    AddTalkListDataIf(not GetEventFlag(1047600311), 134, 89001532, -1)
    AddTalkListDataIf(GetEventFlag(1047600311) == 1, 534, 89001532, -1)
    AddTalkListDataIf(not GetEventFlag(1047600291), 135, 89001533, -1)
    AddTalkListDataIf(GetEventFlag(1047600291) == 1, 535, 89001533, -1)
    AddTalkListDataIf(not GetEventFlag(1047600125), 136, 89001534, -1)
    AddTalkListDataIf(GetEventFlag(1047600125) == 1, 536, 89001534, -1)
    AddTalkListDataIf(not GetEventFlag(1047600319), 137, 89001535, -1)
    AddTalkListDataIf(GetEventFlag(1047600319) == 1, 537, 89001535, -1)
    AddTalkListDataIf(not GetEventFlag(1047600021), 138, 89001536, -1)
    AddTalkListDataIf(GetEventFlag(1047600021) == 1, 538, 89001536, -1)
    AddTalkListDataIf(not GetEventFlag(1047600023), 139, 89001537, -1)
    AddTalkListDataIf(GetEventFlag(1047600023) == 1, 539, 89001537, -1)
    AddTalkListDataIf(not GetEventFlag(1047600117), 140, 89001538, -1)
    AddTalkListDataIf(GetEventFlag(1047600117) == 1, 540, 89001538, -1)
    AddTalkListDataIf(not GetEventFlag(1047600119), 141, 89001539, -1)
    AddTalkListDataIf(GetEventFlag(1047600119) == 1, 541, 89001539, -1)
    AddTalkListDataIf(not GetEventFlag(1047600121), 142, 89001540, -1)
    AddTalkListDataIf(GetEventFlag(1047600121) == 1, 542, 89001540, -1)
    AddTalkListDataIf(not GetEventFlag(1047600055), 143, 89001541, -1)
    AddTalkListDataIf(GetEventFlag(1047600055) == 1, 543, 89001541, -1)
    AddTalkListDataIf(not GetEventFlag(1047600057), 144, 89001542, -1)
    AddTalkListDataIf(GetEventFlag(1047600057) == 1, 544, 89001542, -1)
    AddTalkListDataIf(not GetEventFlag(1047600099), 145, 89001543, -1)
    AddTalkListDataIf(GetEventFlag(1047600099) == 1, 545, 89001543, -1)
    AddTalkListDataIf(not GetEventFlag(1047600199), 146, 89001544, -1)
    AddTalkListDataIf(GetEventFlag(1047600199) == 1, 546, 89001544, -1)
    AddTalkListDataIf(not GetEventFlag(1047600201), 147, 89001545, -1)
    AddTalkListDataIf(GetEventFlag(1047600201) == 1, 547, 89001545, -1)
    AddTalkListDataIf(not GetEventFlag(1047600017), 148, 89001546, -1)
    AddTalkListDataIf(GetEventFlag(1047600017) == 1, 548, 89001546, -1)
    AddTalkListDataIf(not GetEventFlag(1047600019), 149, 89001547, -1)
    AddTalkListDataIf(GetEventFlag(1047600019) == 1, 549, 89001547, -1)
    AddTalkListDataIf(not GetEventFlag(1047600025), 150, 89001548, -1)
    AddTalkListDataIf(GetEventFlag(1047600025) == 1, 550, 89001548, -1)
    AddTalkListDataIf(not GetEventFlag(1047600027), 151, 89001549, -1)
    AddTalkListDataIf(GetEventFlag(1047600027) == 1, 551, 89001549, -1)
    AddTalkListDataIf(not GetEventFlag(1047600235), 152, 89001550, -1)
    AddTalkListDataIf(GetEventFlag(1047600235) == 1, 552, 89001550, -1)
    AddTalkListDataIf(not GetEventFlag(1047600237), 153, 89001551, -1)
    AddTalkListDataIf(GetEventFlag(1047600237) == 1, 553, 89001551, -1)
    AddTalkListDataIf(not GetEventFlag(1047600239), 154, 89001552, -1)
    AddTalkListDataIf(GetEventFlag(1047600239) == 1, 554, 89001552, -1)
    AddTalkListDataIf(not GetEventFlag(1047600293), 155, 89001553, -1)
    AddTalkListDataIf(GetEventFlag(1047600293) == 1, 555, 89001553, -1)
    AddTalkListDataIf(not GetEventFlag(1047600295), 156, 89001554, -1)
    AddTalkListDataIf(GetEventFlag(1047600295) == 1, 556, 89001554, -1)
    AddTalkListDataIf(not GetEventFlag(1047600406), 157, 89001555, -1)
    AddTalkListDataIf(GetEventFlag(1047600406) == 1, 557, 89001555, -1)
    AddTalkListDataIf(not GetEventFlag(1047600408), 158, 89001556, -1)
    AddTalkListDataIf(GetEventFlag(1047600408) == 1, 558, 89001556, -1)
    AddTalkListDataIf(not GetEventFlag(1047600412), 159, 89001557, -1)
    AddTalkListDataIf(GetEventFlag(1047600412) == 1, 559, 89001557, -1)
    AddTalkListDataIf(not GetEventFlag(1047600414), 160, 89001558, -1)
    AddTalkListDataIf(GetEventFlag(1047600414) == 1, 560, 89001558, -1)
    AddTalkListDataIf(not GetEventFlag(1047600035), 161, 89001559, -1)
    AddTalkListDataIf(GetEventFlag(1047600035) == 1, 561, 89001559, -1)
    AddTalkListDataIf(not GetEventFlag(1047600297), 162, 89001560, -1)
    AddTalkListDataIf(GetEventFlag(1047600297) == 1, 562, 89001560, -1)
    AddTalkListDataIf(not GetEventFlag(1047600299), 163, 89001561, -1)
    AddTalkListDataIf(GetEventFlag(1047600299) == 1, 563, 89001561, -1)
    AddTalkListDataIf(not GetEventFlag(1047600229), 164, 89001562, -1)
    AddTalkListDataIf(GetEventFlag(1047600229) == 1, 564, 89001562, -1)
    AddTalkListDataIf(not GetEventFlag(1047600231), 165, 89001563, -1)
    AddTalkListDataIf(GetEventFlag(1047600231) == 1, 565, 89001563, -1)
    AddTalkListDataIf(not GetEventFlag(1047600233), 166, 89001564, -1)
    AddTalkListDataIf(GetEventFlag(1047600233) == 1, 566, 89001564, -1)
    AddTalkListDataIf(not GetEventFlag(1047600317), 167, 89001565, -1)
    AddTalkListDataIf(GetEventFlag(1047600317) == 1, 567, 89001565, -1)
    # action:26080001:"Leave"
    AddTalkListData(999, 26080001, -1)
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if GetTalkListEntryResult() == 101:
        """State 2"""
        assert t608001110_x211(z1=89000020, z2=1047600067, z3=1)
        """State 3"""
        return 0
    elif GetTalkListEntryResult() == 501:
        """State 4"""
        assert t608001110_x211(z1=89000021, z2=1047600067, z3=0)
        """State 5"""
        return 0
    elif GetTalkListEntryResult() == 102:
        """State 6"""
        assert t608001110_x211(z1=89000020, z2=1047600069, z3=1)
        """State 8"""
        return 0
    elif GetTalkListEntryResult() == 502:
        """State 9"""
        assert t608001110_x211(z1=89000021, z2=1047600069, z3=0)
        """State 11"""
        return 0
    elif GetTalkListEntryResult() == 103:
        """State 12"""
        assert t608001110_x211(z1=89000020, z2=1047600154, z3=1)
        """State 13"""
        return 0
    elif GetTalkListEntryResult() == 503:
        """State 14"""
        assert t608001110_x211(z1=89000021, z2=1047600154, z3=0)
        """State 15"""
        return 0
    elif GetTalkListEntryResult() == 104:
        """State 16"""
        assert t608001110_x211(z1=89000020, z2=1047600152, z3=1)
        """State 17"""
        return 0
    elif GetTalkListEntryResult() == 504:
        """State 18"""
        assert t608001110_x211(z1=89000021, z2=1047600152, z3=0)
        """State 19"""
        return 0
    elif GetTalkListEntryResult() == 105:
        """State 20"""
        assert t608001110_x211(z1=89000020, z2=1047600210, z3=1)
        """State 21"""
        return 0
    elif GetTalkListEntryResult() == 505:
        """State 22"""
        assert t608001110_x211(z1=89000021, z2=1047600210, z3=0)
        """State 23"""
        return 0
    elif GetTalkListEntryResult() == 106:
        """State 24"""
        assert t608001110_x211(z1=89000020, z2=1047600265, z3=1)
        """State 25"""
        return 0
    elif GetTalkListEntryResult() == 506:
        """State 26"""
        assert t608001110_x211(z1=89000021, z2=1047600265, z3=0)
        """State 27"""
        return 0
    elif GetTalkListEntryResult() == 107:
        """State 28"""
        assert t608001110_x211(z1=89000020, z2=1047600208, z3=1)
        """State 29"""
        return 0
    elif GetTalkListEntryResult() == 507:
        """State 30"""
        assert t608001110_x211(z1=89000021, z2=1047600208, z3=0)
        """State 31"""
        return 0
    elif GetTalkListEntryResult() == 108:
        """State 32"""
        assert t608001110_x211(z1=89000020, z2=1047600410, z3=1)
        """State 33"""
        return 0
    elif GetTalkListEntryResult() == 508:
        """State 34"""
        assert t608001110_x211(z1=89000021, z2=1047600410, z3=0)
        """State 35"""
        return 0
    elif GetTalkListEntryResult() == 109:
        """State 36"""
        assert t608001110_x211(z1=89000020, z2=1047600142, z3=1)
        """State 37"""
        return 0
    elif GetTalkListEntryResult() == 509:
        """State 38"""
        assert t608001110_x211(z1=89000021, z2=1047600142, z3=0)
        """State 39"""
        return 0
    elif GetTalkListEntryResult() == 110:
        """State 40"""
        assert t608001110_x211(z1=89000020, z2=1047600144, z3=1)
        """State 41"""
        return 0
    elif GetTalkListEntryResult() == 510:
        """State 42"""
        assert t608001110_x211(z1=89000021, z2=1047600144, z3=0)
        """State 43"""
        return 0
    elif GetTalkListEntryResult() == 111:
        """State 44"""
        assert t608001110_x211(z1=89000020, z2=1047600173, z3=1)
        """State 45"""
        return 0
    elif GetTalkListEntryResult() == 511:
        """State 46"""
        assert t608001110_x211(z1=89000021, z2=1047600173, z3=0)
        """State 47"""
        return 0
    elif GetTalkListEntryResult() == 112:
        """State 48"""
        assert t608001110_x211(z1=89000020, z2=1047600175, z3=1)
        """State 49"""
        return 0
    elif GetTalkListEntryResult() == 512:
        """State 50"""
        assert t608001110_x211(z1=89000021, z2=1047600175, z3=0)
        """State 51"""
        return 0
    elif GetTalkListEntryResult() == 113:
        """State 52"""
        assert t608001110_x211(z1=89000020, z2=1047600321, z3=1)
        """State 53"""
        return 0
    elif GetTalkListEntryResult() == 513:
        """State 54"""
        assert t608001110_x211(z1=89000021, z2=1047600321, z3=0)
        """State 55"""
        return 0
    elif GetTalkListEntryResult() == 114:
        """State 56"""
        assert t608001110_x211(z1=89000020, z2=1047600248, z3=1)
        """State 57"""
        return 0
    elif GetTalkListEntryResult() == 514:
        """State 58"""
        assert t608001110_x211(z1=89000021, z2=1047600248, z3=0)
        """State 59"""
        return 0
    elif GetTalkListEntryResult() == 115:
        """State 60"""
        assert t608001110_x211(z1=89000020, z2=1047600140, z3=1)
        """State 61"""
        return 0
    elif GetTalkListEntryResult() == 515:
        """State 62"""
        assert t608001110_x211(z1=89000021, z2=1047600140, z3=0)
        """State 63"""
        return 0
    elif GetTalkListEntryResult() == 116:
        """State 64"""
        assert t608001110_x211(z1=89000020, z2=1047600339, z3=1)
        """State 65"""
        return 0
    elif GetTalkListEntryResult() == 516:
        """State 66"""
        assert t608001110_x211(z1=89000021, z2=1047600339, z3=0)
        """State 67"""
        return 0
    elif GetTalkListEntryResult() == 117:
        """State 68"""
        assert t608001110_x211(z1=89000020, z2=1047600091, z3=1)
        """State 69"""
        return 0
    elif GetTalkListEntryResult() == 517:
        """State 70"""
        assert t608001110_x211(z1=89000021, z2=1047600091, z3=0)
        """State 71"""
        return 0
    elif GetTalkListEntryResult() == 118:
        """State 72"""
        assert t608001110_x211(z1=89000020, z2=1047600093, z3=1)
        """State 73"""
        return 0
    elif GetTalkListEntryResult() == 518:
        """State 74"""
        assert t608001110_x211(z1=89000021, z2=1047600093, z3=0)
        """State 75"""
        return 0
    elif GetTalkListEntryResult() == 119:
        """State 76"""
        assert t608001110_x211(z1=89000020, z2=1047600307, z3=1)
        """State 77"""
        return 0
    elif GetTalkListEntryResult() == 519:
        """State 78"""
        assert t608001110_x211(z1=89000021, z2=1047600307, z3=0)
        """State 79"""
        return 0
    elif GetTalkListEntryResult() == 120:
        """State 80"""
        assert t608001110_x211(z1=89000020, z2=1047600309, z3=1)
        """State 81"""
        return 0
    elif GetTalkListEntryResult() == 520:
        """State 82"""
        assert t608001110_x211(z1=89000021, z2=1047600309, z3=0)
        """State 83"""
        return 0
    elif GetTalkListEntryResult() == 121:
        """State 84"""
        assert t608001110_x211(z1=89000020, z2=1047600268, z3=1)
        """State 85"""
        return 0
    elif GetTalkListEntryResult() == 521:
        """State 86"""
        assert t608001110_x211(z1=89000021, z2=1047600268, z3=0)
        """State 87"""
        return 0
    elif GetTalkListEntryResult() == 122:
        """State 88"""
        assert t608001110_x211(z1=89000020, z2=1047600270, z3=1)
        """State 89"""
        return 0
    elif GetTalkListEntryResult() == 522:
        """State 90"""
        assert t608001110_x211(z1=89000021, z2=1047600270, z3=0)
        """State 91"""
        return 0
    elif GetTalkListEntryResult() == 123:
        """State 92"""
        assert t608001110_x211(z1=89000020, z2=1047600136, z3=1)
        """State 93"""
        return 0
    elif GetTalkListEntryResult() == 523:
        """State 94"""
        assert t608001110_x211(z1=89000021, z2=1047600136, z3=0)
        """State 95"""
        return 0
    elif GetTalkListEntryResult() == 124:
        """State 96"""
        assert t608001110_x211(z1=89000020, z2=1047600272, z3=1)
        """State 97"""
        return 0
    elif GetTalkListEntryResult() == 524:
        """State 98"""
        assert t608001110_x211(z1=89000021, z2=1047600272, z3=0)
        """State 99"""
        return 0
    elif GetTalkListEntryResult() == 125:
        """State 100"""
        assert t608001110_x211(z1=89000020, z2=1047600274, z3=1)
        """State 101"""
        return 0
    elif GetTalkListEntryResult() == 525:
        """State 102"""
        assert t608001110_x211(z1=89000021, z2=1047600274, z3=0)
        """State 103"""
        return 0
    elif GetTalkListEntryResult() == 126:
        """State 104"""
        assert t608001110_x211(z1=89000020, z2=1047600138, z3=1)
        """State 105"""
        return 0
    elif GetTalkListEntryResult() == 526:
        """State 106"""
        assert t608001110_x211(z1=89000021, z2=1047600138, z3=0)
        """State 107"""
        return 0
    elif GetTalkListEntryResult() == 127:
        """State 108"""
        assert t608001110_x211(z1=89000020, z2=1047600313, z3=1)
        """State 109"""
        return 0
    elif GetTalkListEntryResult() == 527:
        """State 110"""
        assert t608001110_x211(z1=89000021, z2=1047600313, z3=0)
        """State 111"""
        return 0
    elif GetTalkListEntryResult() == 128:
        """State 112"""
        assert t608001110_x211(z1=89000020, z2=1047600315, z3=1)
        """State 113"""
        return 0
    elif GetTalkListEntryResult() == 528:
        """State 114"""
        assert t608001110_x211(z1=89000021, z2=1047600315, z3=0)
        """State 115"""
        return 0
    elif GetTalkListEntryResult() == 129:
        """State 116"""
        assert t608001110_x211(z1=89000020, z2=1047600013, z3=1)
        """State 117"""
        return 0
    elif GetTalkListEntryResult() == 529:
        """State 118"""
        assert t608001110_x211(z1=89000021, z2=1047600013, z3=0)
        """State 119"""
        return 0
    elif GetTalkListEntryResult() == 130:
        """State 120"""
        assert t608001110_x211(z1=89000020, z2=1047600015, z3=1)
        """State 121"""
        return 0
    elif GetTalkListEntryResult() == 530:
        """State 122"""
        assert t608001110_x211(z1=89000021, z2=1047600015, z3=0)
        """State 123"""
        return 0
    elif GetTalkListEntryResult() == 131:
        """State 124"""
        assert t608001110_x211(z1=89000020, z2=1047600168, z3=1)
        """State 125"""
        return 0
    elif GetTalkListEntryResult() == 531:
        """State 126"""
        assert t608001110_x211(z1=89000021, z2=1047600168, z3=0)
        """State 127"""
        return 0
    elif GetTalkListEntryResult() == 132:
        """State 128"""
        assert t608001110_x211(z1=89000020, z2=1047600170, z3=1)
        """State 129"""
        return 0
    elif GetTalkListEntryResult() == 532:
        """State 130"""
        assert t608001110_x211(z1=89000021, z2=1047600170, z3=0)
        """State 131"""
        return 0
    elif GetTalkListEntryResult() == 133:
        """State 132"""
        assert t608001110_x211(z1=89000020, z2=1047600171, z3=1)
        """State 133"""
        return 0
    elif GetTalkListEntryResult() == 533:
        """State 134"""
        assert t608001110_x211(z1=89000021, z2=1047600171, z3=0)
        """State 135"""
        return 0
    elif GetTalkListEntryResult() == 134:
        """State 136"""
        assert t608001110_x211(z1=89000020, z2=1047600311, z3=1)
        """State 137"""
        return 0
    elif GetTalkListEntryResult() == 534:
        """State 138"""
        assert t608001110_x211(z1=89000021, z2=1047600311, z3=0)
        """State 139"""
        return 0
    elif GetTalkListEntryResult() == 135:
        """State 140"""
        assert t608001110_x211(z1=89000020, z2=1047600291, z3=1)
        """State 141"""
        return 0
    elif GetTalkListEntryResult() == 535:
        """State 142"""
        assert t608001110_x211(z1=89000021, z2=1047600291, z3=0)
        """State 143"""
        return 0
    elif GetTalkListEntryResult() == 136:
        """State 144"""
        assert t608001110_x211(z1=89000020, z2=1047600125, z3=1)
        """State 145"""
        return 0
    elif GetTalkListEntryResult() == 536:
        """State 146"""
        assert t608001110_x211(z1=89000021, z2=1047600125, z3=0)
        """State 147"""
        return 0
    elif GetTalkListEntryResult() == 137:
        """State 148"""
        assert t608001110_x211(z1=89000020, z2=1047600319, z3=1)
        """State 149"""
        return 0
    elif GetTalkListEntryResult() == 537:
        """State 150"""
        assert t608001110_x211(z1=89000021, z2=1047600319, z3=0)
        """State 151"""
        return 0
    elif GetTalkListEntryResult() == 138:
        """State 152"""
        assert t608001110_x211(z1=89000020, z2=1047600021, z3=1)
        """State 153"""
        return 0
    elif GetTalkListEntryResult() == 538:
        """State 154"""
        assert t608001110_x211(z1=89000021, z2=1047600021, z3=0)
        """State 155"""
        return 0
    elif GetTalkListEntryResult() == 139:
        """State 156"""
        assert t608001110_x211(z1=89000020, z2=1047600023, z3=1)
        """State 157"""
        return 0
    elif GetTalkListEntryResult() == 539:
        """State 158"""
        assert t608001110_x211(z1=89000021, z2=1047600023, z3=0)
        """State 159"""
        return 0
    elif GetTalkListEntryResult() == 140:
        """State 160"""
        assert t608001110_x211(z1=89000020, z2=1047600117, z3=1)
        """State 161"""
        return 0
    elif GetTalkListEntryResult() == 540:
        """State 162"""
        assert t608001110_x211(z1=89000021, z2=1047600117, z3=0)
        """State 163"""
        return 0
    elif GetTalkListEntryResult() == 141:
        """State 164"""
        assert t608001110_x211(z1=89000020, z2=1047600119, z3=1)
        """State 165"""
        return 0
    elif GetTalkListEntryResult() == 541:
        """State 166"""
        assert t608001110_x211(z1=89000021, z2=1047600119, z3=0)
        """State 167"""
        return 0
    elif GetTalkListEntryResult() == 142:
        """State 168"""
        assert t608001110_x211(z1=89000020, z2=1047600121, z3=1)
        """State 169"""
        return 0
    elif GetTalkListEntryResult() == 542:
        """State 170"""
        assert t608001110_x211(z1=89000021, z2=1047600121, z3=0)
        """State 171"""
        return 0
    elif GetTalkListEntryResult() == 143:
        """State 172"""
        assert t608001110_x211(z1=89000020, z2=1047600055, z3=1)
        """State 173"""
        return 0
    elif GetTalkListEntryResult() == 543:
        """State 174"""
        assert t608001110_x211(z1=89000021, z2=1047600055, z3=0)
        """State 175"""
        return 0
    elif GetTalkListEntryResult() == 144:
        """State 176"""
        assert t608001110_x211(z1=89000020, z2=1047600057, z3=1)
        """State 177"""
        return 0
    elif GetTalkListEntryResult() == 544:
        """State 178"""
        assert t608001110_x211(z1=89000021, z2=1047600057, z3=0)
        """State 179"""
        return 0
    elif GetTalkListEntryResult() == 145:
        """State 180"""
        assert t608001110_x211(z1=89000020, z2=1047600099, z3=1)
        """State 181"""
        return 0
    elif GetTalkListEntryResult() == 545:
        """State 182"""
        assert t608001110_x211(z1=89000021, z2=1047600099, z3=0)
        """State 183"""
        return 0
    elif GetTalkListEntryResult() == 146:
        """State 184"""
        assert t608001110_x211(z1=89000020, z2=1047600199, z3=1)
        """State 185"""
        return 0
    elif GetTalkListEntryResult() == 546:
        """State 186"""
        assert t608001110_x211(z1=89000021, z2=1047600199, z3=0)
        """State 187"""
        return 0
    elif GetTalkListEntryResult() == 147:
        """State 188"""
        assert t608001110_x211(z1=89000020, z2=1047600201, z3=1)
        """State 189"""
        return 0
    elif GetTalkListEntryResult() == 547:
        """State 190"""
        assert t608001110_x211(z1=89000021, z2=1047600201, z3=0)
        """State 191"""
        return 0
    elif GetTalkListEntryResult() == 148:
        """State 192"""
        assert t608001110_x211(z1=89000020, z2=1047600017, z3=1)
        """State 193"""
        return 0
    elif GetTalkListEntryResult() == 548:
        """State 194"""
        assert t608001110_x211(z1=89000021, z2=1047600017, z3=0)
        """State 195"""
        return 0
    elif GetTalkListEntryResult() == 149:
        """State 196"""
        assert t608001110_x211(z1=89000020, z2=1047600019, z3=1)
        """State 197"""
        return 0
    elif GetTalkListEntryResult() == 549:
        """State 198"""
        assert t608001110_x211(z1=89000021, z2=1047600019, z3=0)
        """State 199"""
        return 0
    elif GetTalkListEntryResult() == 150:
        """State 200"""
        assert t608001110_x211(z1=89000020, z2=1047600025, z3=1)
        """State 201"""
        return 0
    elif GetTalkListEntryResult() == 550:
        """State 202"""
        assert t608001110_x211(z1=89000021, z2=1047600025, z3=0)
        """State 203"""
        return 0
    elif GetTalkListEntryResult() == 151:
        """State 204"""
        assert t608001110_x211(z1=89000020, z2=1047600027, z3=1)
        """State 205"""
        return 0
    elif GetTalkListEntryResult() == 551:
        """State 206"""
        assert t608001110_x211(z1=89000021, z2=1047600027, z3=0)
        """State 207"""
        return 0
    elif GetTalkListEntryResult() == 152:
        """State 208"""
        assert t608001110_x211(z1=89000020, z2=1047600235, z3=1)
        """State 209"""
        return 0
    elif GetTalkListEntryResult() == 552:
        """State 210"""
        assert t608001110_x211(z1=89000021, z2=1047600235, z3=0)
        """State 211"""
        return 0
    elif GetTalkListEntryResult() == 153:
        """State 212"""
        assert t608001110_x211(z1=89000020, z2=1047600237, z3=1)
        """State 213"""
        return 0
    elif GetTalkListEntryResult() == 553:
        """State 214"""
        assert t608001110_x211(z1=89000021, z2=1047600237, z3=0)
        """State 215"""
        return 0
    elif GetTalkListEntryResult() == 154:
        """State 216"""
        assert t608001110_x211(z1=89000020, z2=1047600239, z3=1)
        """State 217"""
        return 0
    elif GetTalkListEntryResult() == 554:
        """State 218"""
        assert t608001110_x211(z1=89000021, z2=1047600239, z3=0)
        """State 219"""
        return 0
    elif GetTalkListEntryResult() == 155:
        """State 220"""
        assert t608001110_x211(z1=89000020, z2=1047600293, z3=1)
        """State 221"""
        return 0
    elif GetTalkListEntryResult() == 555:
        """State 222"""
        assert t608001110_x211(z1=89000021, z2=1047600293, z3=0)
        """State 223"""
        return 0
    elif GetTalkListEntryResult() == 156:
        """State 224"""
        assert t608001110_x211(z1=89000020, z2=1047600295, z3=1)
        """State 225"""
        return 0
    elif GetTalkListEntryResult() == 556:
        """State 226"""
        assert t608001110_x211(z1=89000021, z2=1047600295, z3=0)
        """State 227"""
        return 0
    elif GetTalkListEntryResult() == 157:
        """State 228"""
        assert t608001110_x211(z1=89000020, z2=1047600406, z3=1)
        """State 229"""
        return 0
    elif GetTalkListEntryResult() == 557:
        """State 230"""
        assert t608001110_x211(z1=89000021, z2=1047600406, z3=0)
        """State 231"""
        return 0
    elif GetTalkListEntryResult() == 158:
        """State 232"""
        assert t608001110_x211(z1=89000020, z2=1047600408, z3=1)
        """State 233"""
        return 0
    elif GetTalkListEntryResult() == 558:
        """State 234"""
        assert t608001110_x211(z1=89000021, z2=1047600408, z3=0)
        """State 235"""
        return 0
    elif GetTalkListEntryResult() == 159:
        """State 236"""
        assert t608001110_x211(z1=89000020, z2=1047600412, z3=1)
        """State 237"""
        return 0
    elif GetTalkListEntryResult() == 559:
        """State 238"""
        assert t608001110_x211(z1=89000021, z2=1047600412, z3=0)
        """State 239"""
        return 0
    elif GetTalkListEntryResult() == 160:
        """State 240"""
        assert t608001110_x211(z1=89000020, z2=1047600414, z3=1)
        """State 241"""
        return 0
    elif GetTalkListEntryResult() == 560:
        """State 242"""
        assert t608001110_x211(z1=89000021, z2=1047600414, z3=0)
        """State 243"""
        return 0
    elif GetTalkListEntryResult() == 161:
        """State 244"""
        assert t608001110_x211(z1=89000020, z2=1047600035, z3=1)
        """State 245"""
        return 0
    elif GetTalkListEntryResult() == 561:
        """State 246"""
        assert t608001110_x211(z1=89000021, z2=1047600035, z3=0)
        """State 247"""
        return 0
    elif GetTalkListEntryResult() == 162:
        """State 248"""
        assert t608001110_x211(z1=89000020, z2=1047600297, z3=1)
        """State 249"""
        return 0
    elif GetTalkListEntryResult() == 562:
        """State 250"""
        assert t608001110_x211(z1=89000021, z2=1047600297, z3=0)
        """State 251"""
        return 0
    elif GetTalkListEntryResult() == 163:
        """State 252"""
        assert t608001110_x211(z1=89000020, z2=1047600299, z3=1)
        """State 253"""
        return 0
    elif GetTalkListEntryResult() == 563:
        """State 254"""
        assert t608001110_x211(z1=89000021, z2=1047600299, z3=0)
        """State 255"""
        return 0
    elif GetTalkListEntryResult() == 164:
        """State 256"""
        assert t608001110_x211(z1=89000020, z2=1047600229, z3=1)
        """State 257"""
        return 0
    elif GetTalkListEntryResult() == 564:
        """State 258"""
        assert t608001110_x211(z1=89000021, z2=1047600229, z3=0)
        """State 259"""
        return 0
    elif GetTalkListEntryResult() == 165:
        """State 260"""
        assert t608001110_x211(z1=89000020, z2=1047600231, z3=1)
        """State 261"""
        return 0
    elif GetTalkListEntryResult() == 565:
        """State 262"""
        assert t608001110_x211(z1=89000021, z2=1047600231, z3=0)
        """State 263"""
        return 0
    elif GetTalkListEntryResult() == 166:
        """State 264"""
        assert t608001110_x211(z1=89000020, z2=1047600233, z3=1)
        """State 265"""
        return 0
    elif GetTalkListEntryResult() == 566:
        """State 266"""
        assert t608001110_x211(z1=89000021, z2=1047600233, z3=0)
        """State 267"""
        return 0
    elif GetTalkListEntryResult() == 167:
        """State 268"""
        assert t608001110_x211(z1=89000020, z2=1047600317, z3=1)
        """State 269"""
        return 0
    elif GetTalkListEntryResult() == 567:
        """State 270"""
        assert t608001110_x211(z1=89000021, z2=1047600317, z3=0)
        """State 271"""
        return 0
    else:
        """State 7,10"""
        return 0

def t608001110_x200(z7=_):
    """State 0,1"""
    OpenGenericDialog(8, z7, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t608001110_x210(z4=_, z5=_, z6=_):
    """State 0"""
    assert t608001110_x220()
    """State 1"""
    SetEventFlag(z5, z6)
    SetEventFlag(1047610101, 1)
    return 0

def t608001110_x211(z1=_, z2=_, z3=_):
    """State 0"""
    assert t608001110_x221()
    """State 1"""
    SetEventFlag(z2, z3)
    SetEventFlag(1047610101, 1)
    return 0

def t608001110_x220():
    """State 0"""
    SetEventFlag(1047600998, 0)
    SetEventFlag(1047600344, 0)
    SetEventFlag(1047600126, 0)
    SetEventFlag(1047600202, 0)
    SetEventFlag(1047600211, 0)
    SetEventFlag(1047600240, 0)
    SetEventFlag(1047600241, 0)
    SetEventFlag(1047600243, 0)
    SetEventFlag(1047600244, 0)
    SetEventFlag(1047600245, 0)
    SetEventFlag(1047600246, 0)
    SetEventFlag(1047600249, 0)
    SetEventFlag(1047600266, 0)
    SetEventFlag(1047600279, 0)
    SetEventFlag(1047600324, 0)
    SetEventFlag(1047600325, 0)
    SetEventFlag(1047600326, 0)
    SetEventFlag(1047600327, 0)
    SetEventFlag(1047600328, 0)
    SetEventFlag(1047600329, 0)
    SetEventFlag(1047600330, 0)
    SetEventFlag(1047600333, 0)
    SetEventFlag(1047600336, 0)
    SetEventFlag(1047600337, 0)
    SetEventFlag(1047600340, 0)
    SetEventFlag(1047600341, 0)
    SetEventFlag(1047600347, 0)
    SetEventFlag(1047600400, 0)
    SetEventFlag(1047600401, 0)
    SetEventFlag(1047600402, 0)
    SetEventFlag(1047600403, 0)
    SetEventFlag(1047600404, 0)
    SetEventFlag(1047600419, 0)
    SetEventFlag(1047600420, 0)
    SetEventFlag(1047600422, 0)
    SetEventFlag(1047600182, 0)
    SetEventFlag(1047600028, 0)
    SetEventFlag(1047600112, 0)
    SetEventFlag(1047600114, 0)
    SetEventFlag(1047600176, 0)
    SetEventFlag(1047600178, 0)
    SetEventFlag(1047600300, 0)
    SetEventFlag(1047600072, 0)
    SetEventFlag(1047600074, 0)
    SetEventFlag(1047600220, 0)
    SetEventFlag(1047600222, 0)
    SetEventFlag(1047600203, 0)
    SetEventFlag(1047600205, 0)
    SetEventFlag(1047600046, 0)
    SetEventFlag(1047600048, 0)
    SetEventFlag(1047600131, 0)
    SetEventFlag(1047600133, 0)
    SetEventFlag(1047600070, 0)
    SetEventFlag(1047600008, 0)
    SetEventFlag(1047600010, 0)
    SetEventFlag(1047600145, 0)
    SetEventFlag(1047600147, 0)
    SetEventFlag(1047600149, 0)
    SetEventFlag(1047600076, 0)
    SetEventFlag(1047600078, 0)
    SetEventFlag(1047600104, 0)
    SetEventFlag(1047600106, 0)
    SetEventFlag(1047600036, 0)
    SetEventFlag(1047600038, 0)
    SetEventFlag(1047600058, 0)
    SetEventFlag(1047600060, 0)
    SetEventFlag(1047600212, 0)
    SetEventFlag(1047600214, 0)
    SetEventFlag(1047600159, 0)
    SetEventFlag(1047600161, 0)
    SetEventFlag(1047600180, 0)
    SetEventFlag(1047600184, 0)
    SetEventFlag(1047600368, 0)
    SetEventFlag(1047600370, 0)
    SetEventFlag(1047600050, 0)
    SetEventFlag(1047600052, 0)
    SetEventFlag(1047600364, 0)
    SetEventFlag(1047600366, 0)
    SetEventFlag(1047600376, 0)
    SetEventFlag(1047600378, 0)
    SetEventFlag(1047600360, 0)
    SetEventFlag(1047600362, 0)
    SetEventFlag(1047600372, 0)
    SetEventFlag(1047600374, 0)
    SetEventFlag(1047600384, 0)
    SetEventFlag(1047600386, 0)
    SetEventFlag(1047600110, 0)
    SetEventFlag(1047600108, 0)
    SetEventFlag(1047600155, 0)
    SetEventFlag(1047600157, 0)
    SetEventFlag(1047600196, 0)
    SetEventFlag(1047600224, 0)
    SetEventFlag(1047600226, 0)
    SetEventFlag(1047600345, 0)
    SetEventFlag(1047600286, 0)
    SetEventFlag(1047600288, 0)
    SetEventFlag(1047600302, 0)
    SetEventFlag(1047600304, 0)
    SetEventFlag(1047600348, 0)
    SetEventFlag(1047600350, 0)
    SetEventFlag(1047600352, 0)
    SetEventFlag(1047600354, 0)
    SetEventFlag(1047600358, 0)
    SetEventFlag(1047600250, 0)
    SetEventFlag(1047600252, 0)
    SetEventFlag(1047600186, 0)
    SetEventFlag(1047600188, 0)
    SetEventFlag(1047600380, 0)
    SetEventFlag(1047600382, 0)
    SetEventFlag(1047600282, 0)
    SetEventFlag(1047600284, 0)
    SetEventFlag(1047600004, 0)
    SetEventFlag(1047600006, 0)
    SetEventFlag(1047600040, 0)
    SetEventFlag(1047600042, 0)
    SetEventFlag(1047600044, 0)
    SetEventFlag(1047600127, 0)
    SetEventFlag(1047600129, 0)
    SetEventFlag(1047600030, 0)
    SetEventFlag(1047600032, 0)
    SetEventFlag(1047600331, 0)
    SetEventFlag(1047600000, 0)
    SetEventFlag(1047600002, 0)
    SetEventFlag(1047600356, 0)
    SetEventFlag(1047600062, 0)
    SetEventFlag(1047600064, 0)
    SetEventFlag(1047600322, 0)
    SetEventFlag(1047600216, 0)
    SetEventFlag(1047600218, 0)
    SetEventFlag(1047600100, 0)
    SetEventFlag(1047600102, 0)
    SetEventFlag(1047600094, 0)
    SetEventFlag(1047600096, 0)
    SetEventFlag(1047600254, 0)
    SetEventFlag(1047600256, 0)
    SetEventFlag(1047600258, 0)
    SetEventFlag(1047600388, 0)
    SetEventFlag(1047600390, 0)
    SetEventFlag(1047600392, 0)
    SetEventFlag(1047600394, 0)
    SetEventFlag(1047600396, 0)
    SetEventFlag(1047600084, 0)
    SetEventFlag(1047600086, 0)
    SetEventFlag(1047600088, 0)
    SetEventFlag(1047600260, 0)
    SetEventFlag(1047600262, 0)
    SetEventFlag(1047600080, 0)
    SetEventFlag(1047600082, 0)
    SetEventFlag(1047600122, 0)
    SetEventFlag(1047600163, 0)
    SetEventFlag(1047600165, 0)
    SetEventFlag(1047600190, 0)
    SetEventFlag(1047600398, 0)
    SetEventFlag(1047600342, 0)
    SetEventFlag(1047600192, 0)
    SetEventFlag(1047600194, 0)
    SetEventFlag(1047600280, 0)
    SetEventFlag(1047600275, 0)
    SetEventFlag(1047600277, 0)
    SetEventFlag(1047600415, 0)
    SetEventFlag(1047600417, 0)
    SetEventFlag(1047600066, 0)
    SetEventFlag(1047600068, 0)
    SetEventFlag(1047600153, 0)
    SetEventFlag(1047600151, 0)
    SetEventFlag(1047600209, 0)
    SetEventFlag(1047600264, 0)
    SetEventFlag(1047600207, 0)
    SetEventFlag(1047600409, 0)
    SetEventFlag(1047600141, 0)
    SetEventFlag(1047600143, 0)
    SetEventFlag(1047600172, 0)
    SetEventFlag(1047600174, 0)
    SetEventFlag(1047600320, 0)
    SetEventFlag(1047600247, 0)
    SetEventFlag(1047600139, 0)
    SetEventFlag(1047600338, 0)
    SetEventFlag(1047600090, 0)
    SetEventFlag(1047600092, 0)
    SetEventFlag(1047600306, 0)
    SetEventFlag(1047600308, 0)
    SetEventFlag(1047600267, 0)
    SetEventFlag(1047600269, 0)
    SetEventFlag(1047600135, 0)
    SetEventFlag(1047600271, 0)
    SetEventFlag(1047600273, 0)
    SetEventFlag(1047600137, 0)
    SetEventFlag(1047600312, 0)
    SetEventFlag(1047600314, 0)
    SetEventFlag(1047600012, 0)
    SetEventFlag(1047600014, 0)
    SetEventFlag(1047600167, 0)
    SetEventFlag(1047600169, 0)
    SetEventFlag(1047600310, 0)
    SetEventFlag(1047600290, 0)
    SetEventFlag(1047600124, 0)
    SetEventFlag(1047600318, 0)
    SetEventFlag(1047600020, 0)
    SetEventFlag(1047600022, 0)
    SetEventFlag(1047600116, 0)
    SetEventFlag(1047600118, 0)
    SetEventFlag(1047600120, 0)
    SetEventFlag(1047600054, 0)
    SetEventFlag(1047600056, 0)
    SetEventFlag(1047600098, 0)
    SetEventFlag(1047600198, 0)
    SetEventFlag(1047600200, 0)
    SetEventFlag(1047600016, 0)
    SetEventFlag(1047600018, 0)
    SetEventFlag(1047600024, 0)
    SetEventFlag(1047600026, 0)
    SetEventFlag(1047600234, 0)
    SetEventFlag(1047600236, 0)
    SetEventFlag(1047600238, 0)
    SetEventFlag(1047600292, 0)
    SetEventFlag(1047600294, 0)
    SetEventFlag(1047600405, 0)
    SetEventFlag(1047600407, 0)
    SetEventFlag(1047600411, 0)
    SetEventFlag(1047600413, 0)
    SetEventFlag(1047600034, 0)
    SetEventFlag(1047600296, 0)
    SetEventFlag(1047600298, 0)
    SetEventFlag(1047600228, 0)
    SetEventFlag(1047600230, 0)
    SetEventFlag(1047600232, 0)
    SetEventFlag(1047600316, 0)
    SetEventFlag(1047600427, 0)
    SetEventFlag(1047600428, 0)
    SetEventFlag(1047600429, 0)
    SetEventFlag(1047600430, 0)
    return 0

def t608001110_x221():
    """State 0"""
    SetEventFlag(1047600421, 0)
    SetEventFlag(1047600334, 0)
    SetEventFlag(1047600335, 0)
    SetEventFlag(1047600423, 0)
    SetEventFlag(1047600424, 0)
    SetEventFlag(1047600425, 0)
    SetEventFlag(1047600426, 0)
    SetEventFlag(1047600242, 0)
    SetEventFlag(1047600029, 0)
    SetEventFlag(1047600113, 0)
    SetEventFlag(1047600115, 0)
    SetEventFlag(1047600177, 0)
    SetEventFlag(1047600179, 0)
    SetEventFlag(1047600301, 0)
    SetEventFlag(1047600073, 0)
    SetEventFlag(1047600075, 0)
    SetEventFlag(1047600221, 0)
    SetEventFlag(1047600223, 0)
    SetEventFlag(1047600204, 0)
    SetEventFlag(1047600206, 0)
    SetEventFlag(1047600047, 0)
    SetEventFlag(1047600049, 0)
    SetEventFlag(1047600132, 0)
    SetEventFlag(1047600134, 0)
    SetEventFlag(1047600071, 0)
    SetEventFlag(1047600009, 0)
    SetEventFlag(1047600011, 0)
    SetEventFlag(1047600146, 0)
    SetEventFlag(1047600148, 0)
    SetEventFlag(1047600150, 0)
    SetEventFlag(1047600077, 0)
    SetEventFlag(1047600079, 0)
    SetEventFlag(1047600105, 0)
    SetEventFlag(1047600107, 0)
    SetEventFlag(1047600037, 0)
    SetEventFlag(1047600039, 0)
    SetEventFlag(1047600059, 0)
    SetEventFlag(1047600061, 0)
    SetEventFlag(1047600213, 0)
    SetEventFlag(1047600215, 0)
    SetEventFlag(1047600160, 0)
    SetEventFlag(1047600162, 0)
    SetEventFlag(1047600181, 0)
    SetEventFlag(1047600185, 0)
    SetEventFlag(1047600369, 0)
    SetEventFlag(1047600371, 0)
    SetEventFlag(1047600051, 0)
    SetEventFlag(1047600053, 0)
    SetEventFlag(1047600365, 0)
    SetEventFlag(1047600367, 0)
    SetEventFlag(1047600377, 0)
    SetEventFlag(1047600379, 0)
    SetEventFlag(1047600361, 0)
    SetEventFlag(1047600363, 0)
    SetEventFlag(1047600373, 0)
    SetEventFlag(1047600375, 0)
    SetEventFlag(1047600385, 0)
    SetEventFlag(1047600387, 0)
    SetEventFlag(1047600111, 0)
    SetEventFlag(1047600109, 0)
    SetEventFlag(1047600156, 0)
    SetEventFlag(1047600158, 0)
    SetEventFlag(1047600197, 0)
    SetEventFlag(1047600225, 0)
    SetEventFlag(1047600227, 0)
    SetEventFlag(1047600346, 0)
    SetEventFlag(1047600287, 0)
    SetEventFlag(1047600289, 0)
    SetEventFlag(1047600303, 0)
    SetEventFlag(1047600305, 0)
    SetEventFlag(1047600349, 0)
    SetEventFlag(1047600351, 0)
    SetEventFlag(1047600353, 0)
    SetEventFlag(1047600355, 0)
    SetEventFlag(1047600359, 0)
    SetEventFlag(1047600251, 0)
    SetEventFlag(1047600253, 0)
    SetEventFlag(1047600187, 0)
    SetEventFlag(1047600189, 0)
    SetEventFlag(1047600381, 0)
    SetEventFlag(1047600383, 0)
    SetEventFlag(1047600283, 0)
    SetEventFlag(1047600285, 0)
    SetEventFlag(1047600005, 0)
    SetEventFlag(1047600007, 0)
    SetEventFlag(1047600041, 0)
    SetEventFlag(1047600043, 0)
    SetEventFlag(1047600045, 0)
    SetEventFlag(1047600128, 0)
    SetEventFlag(1047600130, 0)
    SetEventFlag(1047600031, 0)
    SetEventFlag(1047600033, 0)
    SetEventFlag(1047600332, 0)
    SetEventFlag(1047600001, 0)
    SetEventFlag(1047600003, 0)
    SetEventFlag(1047600357, 0)
    SetEventFlag(1047600063, 0)
    SetEventFlag(1047600065, 0)
    SetEventFlag(1047600323, 0)
    SetEventFlag(1047600217, 0)
    SetEventFlag(1047600219, 0)
    SetEventFlag(1047600101, 0)
    SetEventFlag(1047600103, 0)
    SetEventFlag(1047600095, 0)
    SetEventFlag(1047600097, 0)
    SetEventFlag(1047600255, 0)
    SetEventFlag(1047600257, 0)
    SetEventFlag(1047600259, 0)
    SetEventFlag(1047600389, 0)
    SetEventFlag(1047600391, 0)
    SetEventFlag(1047600393, 0)
    SetEventFlag(1047600395, 0)
    SetEventFlag(1047600397, 0)
    SetEventFlag(1047600085, 0)
    SetEventFlag(1047600087, 0)
    SetEventFlag(1047600089, 0)
    SetEventFlag(1047600261, 0)
    SetEventFlag(1047600263, 0)
    SetEventFlag(1047600081, 0)
    SetEventFlag(1047600083, 0)
    SetEventFlag(1047600123, 0)
    SetEventFlag(1047600164, 0)
    SetEventFlag(1047600166, 0)
    SetEventFlag(1047600191, 0)
    SetEventFlag(1047600399, 0)
    SetEventFlag(1047600343, 0)
    SetEventFlag(1047600193, 0)
    SetEventFlag(1047600195, 0)
    SetEventFlag(1047600281, 0)
    SetEventFlag(1047600276, 0)
    SetEventFlag(1047600278, 0)
    SetEventFlag(1047600416, 0)
    SetEventFlag(1047600418, 0)
    SetEventFlag(1047600067, 0)
    SetEventFlag(1047600069, 0)
    SetEventFlag(1047600154, 0)
    SetEventFlag(1047600152, 0)
    SetEventFlag(1047600210, 0)
    SetEventFlag(1047600265, 0)
    SetEventFlag(1047600208, 0)
    SetEventFlag(1047600410, 0)
    SetEventFlag(1047600142, 0)
    SetEventFlag(1047600144, 0)
    SetEventFlag(1047600173, 0)
    SetEventFlag(1047600175, 0)
    SetEventFlag(1047600321, 0)
    SetEventFlag(1047600248, 0)
    SetEventFlag(1047600140, 0)
    SetEventFlag(1047600339, 0)
    SetEventFlag(1047600091, 0)
    SetEventFlag(1047600093, 0)
    SetEventFlag(1047600307, 0)
    SetEventFlag(1047600309, 0)
    SetEventFlag(1047600268, 0)
    SetEventFlag(1047600270, 0)
    SetEventFlag(1047600136, 0)
    SetEventFlag(1047600272, 0)
    SetEventFlag(1047600274, 0)
    SetEventFlag(1047600138, 0)
    SetEventFlag(1047600313, 0)
    SetEventFlag(1047600315, 0)
    SetEventFlag(1047600013, 0)
    SetEventFlag(1047600015, 0)
    SetEventFlag(1047600168, 0)
    SetEventFlag(1047600170, 0)
    SetEventFlag(1047600171, 0)
    SetEventFlag(1047600311, 0)
    SetEventFlag(1047600291, 0)
    SetEventFlag(1047600125, 0)
    SetEventFlag(1047600319, 0)
    SetEventFlag(1047600021, 0)
    SetEventFlag(1047600023, 0)
    SetEventFlag(1047600117, 0)
    SetEventFlag(1047600119, 0)
    SetEventFlag(1047600121, 0)
    SetEventFlag(1047600055, 0)
    SetEventFlag(1047600057, 0)
    SetEventFlag(1047600099, 0)
    SetEventFlag(1047600199, 0)
    SetEventFlag(1047600201, 0)
    SetEventFlag(1047600017, 0)
    SetEventFlag(1047600019, 0)
    SetEventFlag(1047600025, 0)
    SetEventFlag(1047600027, 0)
    SetEventFlag(1047600235, 0)
    SetEventFlag(1047600237, 0)
    SetEventFlag(1047600239, 0)
    SetEventFlag(1047600293, 0)
    SetEventFlag(1047600295, 0)
    SetEventFlag(1047600406, 0)
    SetEventFlag(1047600408, 0)
    SetEventFlag(1047600412, 0)
    SetEventFlag(1047600414, 0)
    SetEventFlag(1047600035, 0)
    SetEventFlag(1047600297, 0)
    SetEventFlag(1047600299, 0)
    SetEventFlag(1047600229, 0)
    SetEventFlag(1047600231, 0)
    SetEventFlag(1047600233, 0)
    SetEventFlag(1047600317, 0)
    SetEventFlag(1047600431, 0)
    return 0

