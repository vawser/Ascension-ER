RegisterTableGoal(GOAL_ProlificRenala203000_Battle, "ProlificRenala203000_Battle")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_ProlificRenala203000_Battle, true)

Goal.Initialize = function (f1_arg0, f1_arg1, f1_arg2, f1_arg3)
    
end

Goal.Activate = function (f2_arg0, f2_arg1, f2_arg2)
    Init_Pseudo_Global(f2_arg1, f2_arg2)
    f2_arg1:SetStringIndexedNumber("Dist_SideStep", 5)
    f2_arg1:SetStringIndexedNumber("Dist_BackStep", 5)
    local f2_local0 = {}
    local f2_local1 = {}
    local f2_local2 = {}
    Common_Clear_Param(f2_local0, f2_local1, f2_local2)
    local f2_local3 = f2_arg1:GetDist(TARGET_ENE_0)
    local f2_local4 = f2_arg1:GetRandam_Int(1, 100)
    local f2_local5 = f2_arg1:GetExcelParam(AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer)
    local f2_local6 = f2_arg1:GetEventRequest()
    f2_arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    f2_arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5026)
    f2_arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5030)
    if f2_arg1:HasSpecialEffectId(TARGET_SELF, 14357) and f2_arg1:HasSpecialEffectId(TARGET_SELF, 14358) == false then
        f2_local0[3] = 100
    elseif f2_arg1:HasSpecialEffectId(TARGET_SELF, 14358) then
        if f2_arg1:HasSpecialEffectId(TARGET_SELF, 14357) then
            f2_local0[1] = 100
        elseif f2_arg1:HasSpecialEffectId(TARGET_SELF, 14356) then
            f2_local0[4] = 100
        end
    elseif f2_arg1:HasSpecialEffectId(TARGET_SELF, 14359) then
        if f2_arg1:GetTimer(0) <= 0 then
            f2_local0[2] = 100
        else
            f2_local0[20] = 100
        end
    else
        f2_local0[20] = 100
    end
    f2_local1[1] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act01)
    f2_local1[2] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act02)
    f2_local1[3] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act03)
    f2_local1[4] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act04)
    f2_local1[20] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act20)
    f2_local1[30] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act30)
    f2_local1[40] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act40)
    f2_local1[41] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act41)
    f2_local1[42] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act42)
    f2_local1[43] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act43)
    f2_local1[44] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act44)
    f2_local1[45] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act45)
    f2_local1[46] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act46)
    f2_local1[47] = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_Act47)
    local f2_local7 = REGIST_FUNC(f2_arg1, f2_arg2, ProlificRenala203000_ActAfter_AdjustSpace)
    Common_Battle_Activate(f2_arg1, f2_arg2, f2_local0, f2_local1, f2_local7, f2_local2)
    
end

function ProlificRenala203000_Act01(f3_arg0, f3_arg1, f3_arg2)
    f3_arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    f3_arg1:AddSubGoal(GOAL_COMMON_Wait, 2, TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act02(f4_arg0, f4_arg1, f4_arg2)
    f4_arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    f4_arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5026)
    local f4_local0 = 40
    local f4_local1 = 3000
    local f4_local2 = 5 - f4_arg0:GetMapHitRadius(TARGET_SELF)
    local f4_local3 = 0
    local f4_local4 = 0
    f4_arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, f4_local0, f4_local1, TARGET_ENE_0, f4_local2, f4_local3, f4_local4, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act03(f5_arg0, f5_arg1, f5_arg2)
    f5_arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    local f5_local0 = 12
    local f5_local1 = 20001
    local f5_local2 = 5 - f5_arg0:GetMapHitRadius(TARGET_SELF)
    local f5_local3 = 0
    local f5_local4 = 0
    f5_arg1:AddSubGoal(GOAL_COMMON_ComboRepeat, f5_local0, f5_local1, TARGET_ENE_0, f5_local2, f5_local3, f5_local4, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act04(f6_arg0, f6_arg1, f6_arg2)
    f6_arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    local f6_local0 = 12
    local f6_local1 = 3011
    local f6_local2 = 5 - f6_arg0:GetMapHitRadius(TARGET_SELF)
    local f6_local3 = 0
    local f6_local4 = 0
    f6_arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, f6_local0, f6_local1, TARGET_ENE_0, f6_local2, f6_local3, f6_local4, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act20(f7_arg0, f7_arg1, f7_arg2)
    local f7_local0 = f7_arg0:GetMovePointNumber()
    local f7_local1 = true
    if f7_local0 >= 0 then
        f7_arg1:AddSubGoal(GOAL_COMMON_MoveToSomewhereSmooth, 1.5, POINT_MOVE_POINT, AI_DIR_TYPE_CENTER, 0, TARGET_SELF, f7_local1)
    else
        f7_arg1:AddSubGoal(GOAL_COMMON_Stay, 10, 0, TARGET_ENE_0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act30(f8_arg0, f8_arg1, f8_arg2)
    f8_arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5030)
    local f8_local0 = 40
    local f8_local1 = 3000
    local f8_local2 = 5 - f8_arg0:GetMapHitRadius(TARGET_SELF)
    local f8_local3 = 0
    local f8_local4 = 0
    f8_arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, f8_local0, f8_local1, TARGET_ENE_0, f8_local2, f8_local3, f8_local4, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act40(f9_arg0, f9_arg1, f9_arg2)
    local f9_local0 = 2
    local f9_local1 = 2
    local f9_local2 = true
    local f9_local3 = -1
    f9_arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, f9_local0, TARGET_ENE_0, f9_local1, TARGET_SELF, f9_local2, f9_local3)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act41(f10_arg0, f10_arg1, f10_arg2)
    local f10_local0 = 2
    local f10_local1 = 8
    local f10_local2 = false
    local f10_local3 = -1
    f10_arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, f10_local0, TARGET_ENE_0, f10_local1, TARGET_SELF, f10_local2, f10_local3)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act42(f11_arg0, f11_arg1, f11_arg2)
    f11_arg1:AddSubGoal(GOAL_COMMON_Turn, 2, TARGET_ENE_0, f11_arg0:GetRandam_Int(15, 20), 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act43(f12_arg0, f12_arg1, f12_arg2)
    local f12_local0 = 1
    local f12_local1 = 0
    local f12_local2 = 100
    local f12_local3 = 0
    local f12_local4 = 0
    local f12_local5 = TARGET_ENE_0
    local f12_local6 = 1
    local f12_local7 = 0
    local f12_local8 = true
    f12_arg1:AddSubGoal(GOAL_COMMON_StepSafety, f12_local0, f12_local1, f12_local2, f12_local3, f12_local4, f12_local5, f12_local6, f12_local7, f12_local8)
    local f12_local9 = f12_arg0:GetDist(TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act44(f13_arg0, f13_arg1, f13_arg2)
    local f13_local0 = f13_arg0:GetRandam_Int(0, 1)
    local f13_local1 = 2
    local f13_local2 = TARGET_ENE_0
    local f13_local3 = f13_local0
    local f13_local4 = 15
    local f13_local5 = true
    local f13_local6 = -1
    local f13_local7 = GUARD_GOAL_DESIRE_RET_Failed
    local f13_local8 = true
    f13_arg1:AddSubGoal(GOAL_COMMON_SidewayMove, f13_local1, f13_local2, f13_local3, f13_local4, f13_local5, isLifeSuccess, f13_local6, f13_local7)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act45(f14_arg0, f14_arg1, f14_arg2)
    local f14_local0 = 6
    local f14_local1 = 15
    local f14_local2 = true
    local f14_local3 = -1
    f14_arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, f14_local0, TARGET_ENE_0, f14_local1, TARGET_SELF, f14_local2, f14_local3)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act46(f15_arg0, f15_arg1, f15_arg2)
    local f15_local0 = 3
    local f15_local1 = TARGET_ENE_0
    local f15_local2 = 8
    local f15_local3 = TARGET_ENE_0
    local f15_local4 = true
    local f15_local5 = -1
    local f15_local6 = GUARD_GOAL_DESIRE_RET_Failed
    local f15_local7 = false
    local f15_local8 = 1
    f15_arg1:AddSubGoal(GOAL_COMMON_LeaveTargetToPathEnd, f15_local0, f15_local1, f15_local2, f15_local3, f15_local4, f15_local5, f15_local6, f15_local7, f15_local8)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_Act47(f16_arg0, f16_arg1, f16_arg2)
    f16_arg1:AddSubGoal(GOAL_COMMON_WalkAround_Anywhere, 10, 0.2, 20, true, -1, 3, 4, false, false)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
    
end

function ProlificRenala203000_ActAfter_AdjustSpace(f17_arg0, f17_arg1, f17_arg2)
    f17_arg1:AddSubGoal(GOAL_ProlificRenala203000_AfterAttackAct, 10)
    
end

Goal.Update = function (f18_arg0, f18_arg1, f18_arg2)
    return Update_Default_NoSubGoal(f18_arg0, f18_arg1, f18_arg2)
    
end

Goal.Terminate = function (f19_arg0, f19_arg1, f19_arg2)
    
end

Goal.Interrupt = function (f20_arg0, f20_arg1, f20_arg2)
    if f20_arg1:IsLadderAct(TARGET_SELF) then
        return false
    end
    local f20_local0 = 5 - f20_arg1:GetMapHitRadius(TARGET_SELF)
    local f20_local1 = 0
    local f20_local2 = 20
    local f20_local3 = f20_arg1:GetDist(TARGET_ENE_0)
    local f20_local4 = f20_arg1:GetRandam_Int(1, 100)
    if f20_arg1:IsInterupt(INTERUPT_Damaged) then
    end
    if f20_arg1:IsInterupt(INTERUPT_ActivateSpecialEffect) then
        if f20_arg1:HasSpecialEffectId(TARGET_SELF, 5026) then
            f20_arg1:SetTimer(0, 40)
            f20_arg2:ClearSubGoal()
            f20_arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, 0, 0, 0, 0, 0)
            return true
        elseif f20_arg1:HasSpecialEffectId(TARGET_SELF, 5030) then
            f20_arg2:ClearSubGoal()
            return true
        end
    end
    return false
    
end

RegisterTableGoal(GOAL_ProlificRenala203000_AfterAttackAct, "ProlificRenala203000_AfterAttackAct")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_ProlificRenala203000_AfterAttackAct, true)

Goal.Update = function (f21_arg0, f21_arg1, f21_arg2)
    return Update_Default_NoSubGoal(f21_arg0, f21_arg1, f21_arg2)
    
end


