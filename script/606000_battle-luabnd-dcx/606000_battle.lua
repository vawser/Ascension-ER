LuaP		¶	hçõ}A       =(none)                              RegisterTableGoal        GOAL_Wildsheep606000_Battle        Wildsheep606000_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate        Wildsheep606000_Act01        Wildsheep606000_Act02        Wildsheep606000_Act03        Wildsheep606000_Act04        Wildsheep606000_Act05        Wildsheep606000_Act06        Wildsheep606000_Act10        Wildsheep606000_Act11        Wildsheep606000_Act12        Wildsheep606000_Act13        Wildsheep606000_Act14        Wildsheep606000_Act15        Wildsheep606000_Act16        Wildsheep606000_Act17        Wildsheep606000_Act18 %       Wildsheep606000_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt $       GOAL_Wildsheep606000_AfterAttackAct        Wildsheep606000_AfterAttackAct            D                           Init_Pseudo_Global        GetStringIndexedNumber        WalkBefore        Alert_mode        TURNING_RANGE        FirstRoll_Flg        RollPathChkMiss        SetStringIndexedNumber         
       SetNumber       ð?              YË¾   YË¾ Á  YË¾  YË¾ A YË¾  YKÀ A  Y KÀ   Y ËÀ   Y           a                 M          FearOfFire        PLAN_SIDEWAYTYPE__NONE        Common_Clear_Param $       DeleteObserveSpecialEffectAttribute        TARGET_SELF      XÆ@     ¡³@     ¢³@       GetDist        TARGET_ENE_0        TARGET_FRI_0        GetRandam_Int       ð?      Y@       GetPrevTargetState        HasSpecialEffectId      YÆ@     ®¿@      6@      9@!       AddObserveSpecialEffectAttribute      ²É@      @     Q@       IsBattleState 
       GetHpRate       à?       GetStringIndexedNumber        RollPathChkMiss               0@      1@       IsInsideTarget        AI_DIR_TYPE_F       ^@      2@      T@      @      ,@      >@ffffffæ?      D@      I@       IsSearchHighState        IsSearchLowState        IsCautionState       @       @      4@      $@      (@
       SetNumber     ZÆ@       SetCoolTime      ¸§@      @       REGIST_FUNC        Wildsheep606000_Act01        Wildsheep606000_Act02        Wildsheep606000_Act03        Wildsheep606000_Act04        Wildsheep606000_Act05        Wildsheep606000_Act06        Wildsheep606000_Act10       &@       Wildsheep606000_Act11        Wildsheep606000_Act12       *@       Wildsheep606000_Act13        Wildsheep606000_Act14       .@       Wildsheep606000_Act15        Wildsheep606000_Act16        Wildsheep606000_Act17        Wildsheep606000_Act18 %       Wildsheep606000_ActAfter_AdjustSpace        Common_Battle_Activate     O        E         
  
  
        	Y K¿  A 	Y K¿   	Y K¿  Á 	Y À E À  	KÁ  
A  Â 	 	KÂ 
 A  
KÂ    KÂ E A  KÂ  A  KÁ    KÁ Á Á  KÁ  A  Ã  A Y KÂ  A    T  IDT   U KÂ  A     Ä  	 ËÄ  Å  KÅ  ÕÅ T  ÉAÔ ÉÁT Æ E E    Ç Ô  IDÉÅIHÔ  Ô  IHIÈÉHT 	I	I KÉ  XÔ É  XÔ  ËÉ  Ô ËÄ  Å  KÅ  ÕÅ T  ÉA
 ÉÁ
 ÉA	 IHÊ	É  U Ô Ä   KÅ  ÕÅ T  ÉA ÉÁ KÉ  XÔ  ËÉ  T  ÉA É  T  ÉA  IHÊ	ÉKÉ      ËÉ     Ô  KË  A Y KÂ         ÉÅE      Á FÇA I     E  I       I     Å  I       I     E  I       I     Å  I     E  I       I       I     E  I     Å  I        I     E  I       I     Å            Y          4                          GetRandam_Int       ð?      Y@       SetStringIndexedNumber        WalkBefore               >@       AddSubGoal        GOAL_COMMON_AttackTunableSpin       @     §@       TARGET_SELF 
       DIST_None      V@      N@#       GOAL_COMMON_ComboAttackTunableSpin      f@       GOAL_COMMON_ComboRepeat      §@       GOAL_COMMON_ComboFinal        GetWellSpace_Odds     h   > A     K?  A Y À T KÀ  A  Å 	 
A A Y Â T KÀ Å A  Å 	 
A  A A YKÀ E A  Å 	 
A A YKÀ Å A  Å 	 
A A Y KÀ Å A  Å 	 
A  A A YKÀ E A  Å 	 
A A YKÀ E A  Å 	 
A A YKÀ E A  Å 	 
A A YKÀ Å A  Å 	 
A A YA              V                          SetStringIndexedNumber        WalkBefore                AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@     §@       TARGET_ENE_0 
       DIST_None      V@       GetWellSpace_Odds        > A    Y K¿  A  Å  	  
A Y               e                "          TARGET_ENE_0        GetCurrTargetState        AI_TARGET_STATE__SEARCH        AI_TARGET_STATE__SEARCH2        TARGET_SEARCH        AI_TARGET_STATE__CAUTION        GetDist        TARGET_SOUND                SetStringIndexedNumber        WalkBefore        AddObserveArea        TARGET_SELF        AI_DIR_TYPE_F      v@      6@       AddSubGoal        GOAL_COMMON_Turn       $@      N@       GOAL_COMMON_AttackTunableSpin       @     §@
       DIST_None      V@      @      4@      ð?      ð¿       AI_DIR_TYPE_CENTER        GOAL_COMMON_ApproachTarget        appDist        Alert_mode        GetWellSpace_Odds     O     Ë>    U Ë>  Å  U T    Ë>  E U @ Å    Å Ë@   Y KA    E 	 
Á Y Â E   Á 	Y Â  A   	Å 
  YA      	 
E Â     Å        YË@  Á Y  G E                                      GetRandam_Int       ð?      Y@       @              $@      @       @       Approach_Act_Flex      p§@       AddSubGoal        GOAL_COMMON_AttackTunableSpin        TARGET_ENE_0       >@       GOAL_COMMON_LeaveTarget       @      ð¿       GetWellSpace_Odds     5   > A     Á   A     	Á 
                 Y A    Á Å A A         YÖÁ  Á  Á   Á    Y G E            ²                         @       TARGET_FRI_0       ð?      ð¿       AI_DIR_TYPE_CENTER        HasSpecialEffectId      YÆ@       AddSubGoal        GOAL_COMMON_ApproachTarget        appDist        GetWellSpace_Odds                  E    E    Á   	 
Ë? E       KÀ     E         YÁ              Ê                          SetStringIndexedNumber        WalkBefore                AddSubGoal        GOAL_COMMON_Wait       @       TARGET_ENE_0        GetWellSpace_Odds        > A    Y K¿  A      	  
Y   Ç Å            Ú                	         ð?       SetStringIndexedNumber        WalkBefore        AddSubGoal         GOAL_COMMON_WalkAround_Anywhere       ð¿      $@               GetWellSpace_Odds          Ë>     Y K¿  A    	 
A Á       Y Á              ï                &         @       GetMapHitRadius        TARGET_SELF        GetRelativeAngleFromTarget        TARGET_ENE_0       ð?      ð¿     v@       GetRandam_Int       Y@       ClearSubGoal        GetDist                TARGET_FRI_0        SetStringIndexedNumber        TURNING_RANGE       .@      4@      N@       AddObserveArea        AI_DIR_TYPE_F        GetStringIndexedNumber        WalkBefore        IsInsideTarget       D@       AddSubGoal        GOAL_COMMON_SpinStep       $@     p·@     q·@       AI_DIR_TYPE_B      r·@      4À     s·@       Alert_mode        GOAL_COMMON_LeaveTarget       I@       GetWellSpace_Odds     |   Ë>   Í }K?   Á @ A 	A 
  Á 	Y 	KA 	 	Á   E B 	Á @  A  Y  	Ã T KC 	      Á ËC Á Y  	ËC 	 	Õ¿ Ô KD 	    		 ËÄ 	 Á @  A       Y	Ô  T ËÄ 	 Á Á      Y	Ô F T ËÄ 	 Á A      Y	Ô ËÄ 	 Á @  A       Y	B 	  Y 	B 	  Y 	ËÄ 	Å Á   	      Y	 	G	 	E	 	 	          1                %         @       GetMapHitRadius        TARGET_SELF       ð?      ð¿     f@       GetRandam_Int       Y@       TARGET_ENE_0        GetCurrTargetState        AI_TARGET_STATE__SEARCH        AI_TARGET_STATE__SEARCH2        TARGET_SEARCH        AI_TARGET_STATE__CAUTION        GetDist        TARGET_SOUND                AI_TARGET_STATE__BATTLE        AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin       ø?     §@    Ã@      à?      N@
       SetNumber       .@       GetExistMeshOnLineDistEx        AI_DIR_TYPE_F        AI_DIR_TYPE_L        AI_DIR_TYPE_R #       GOAL_COMMON_LeaveTarget_Continuous       $@      >@       GUARD_GOAL_DESIRE_RET_Continue        @       GetWellSpace_Odds     ^   Ë>   Í } A @ Á  Á 	  Ë@   	U Ë@  Å 	U T    Ë@  E 	U B Å 
   Å Ë@  E 	U Ã Å 
 A   Á    YËD Á  
Á  Y Ë@  E 	U T B  
Ë> 	  	 
KE    L  @ E   Ã Å   A         Á Y  	 	            r                         @       GetMapHitRadius        TARGET_SELF       ð?      ð¿     f@       GetRandam_Int       Y@       TARGET_ENE_0        GetDist               .@       GetExistMeshOnLineDistEx        AI_DIR_TYPE_F        AI_DIR_TYPE_L        AI_DIR_TYPE_R        AddSubGoal #       GOAL_COMMON_LeaveTarget_Continuous       $@      >@       GUARD_GOAL_DESIRE_RET_Continue        @       GetWellSpace_Odds     4   Ë>   Í } A @ Á  Á 	  Ë@  
A     Ë@  
Ë> 	  	Á 
A   E L  @  Å  Â E   Á         A Y                               	          AddSubGoal        GOAL_COMMON_LeaveTarget       @       TARGET_ENE_0       $@      ð?      ð¿       GetWellSpace_Odds                ¾ E    Å   Å  	  
 Y Ç Å            £                   !       AddObserveSpecialEffectAttribute        TARGET_SELF     ´É@       AddSubGoal        GOAL_COMMON_ApproachTarget        @       TARGET_SOUND        GetRandam_Float       ð?      @      ð¿       GetWellSpace_Odds                > E    Y K¿  A  K@  
A  E  	  
 Y Ç Å            ¸                          SetStringIndexedNumber        FirstRoll_Flg       ð?       AddSubGoal        GOAL_COMMON_LeaveTarget        @       TARGET_ENE_0       D@       TARGET_SELF       ð¿               SetFailedEndOption -       AI_GOAL_FAILED_END_OPT__PARENT_NEXT_SUB_GOAL        IsExistMeshOnLine        AI_DIR_TYPE_F        @!       AddObserveSpecialEffectAttribute      ¡³@       GOAL_COMMON_AttackTunableSpin       $@     ¬§@       GetWellSpace_Odds        RollPathChkMiss     7   > A    Y K¿  A  Á  	  
A   KÁ YËA   Á   Ô B  A Y K¿  Á    	 
   Y G E  Ô >    Y  G E            Õ                          HasSpecialEffectId        TARGET_SELF      (´@     XÆ@       Approach_Act_Flex       ð?             8@      Y@      ð¿      @       AddSubGoal        GOAL_COMMON_AttackTunableSpin      p§@       TARGET_ENE_0 #       GOAL_COMMON_LeaveTarget_Continuous       $@      >@       GUARD_GOAL_DESIRE_RET_Continue        @       GOAL_COMMON_LeaveTarget_Escape       ø?       GetWellSpace_Odds     ?   > E     
 > E  Á             A  Á  	A 
  Y KÁ  A A   	 
   YT KÁ Å   A E  	  
A    Á Y  KÁ    A E  	  
A Y              î                
   !       AddObserveSpecialEffectAttribute        TARGET_SELF      ¢³@       AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@     ¶§@       TARGET_ENE_0                GetWellSpace_Odds        > E    Y K¿  A  Å  	 
   Y G E            þ                          AddSubGoal $       GOAL_Wildsheep606000_AfterAttackAct       $@       ¾ E    Y                                     Update_Default_NoSubGoal                                                                                   .          GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0        IsLadderAct        TARGET_SELF       9@      $@       Damaged_Act        ClearSubGoal        SetStringIndexedNumber        TURNING_RANGE       .@      4@       AddObserveArea                AI_DIR_TYPE_F      v@       GetStringIndexedNumber        AddSubGoal        GOAL_COMMON_LeaveTarget       I@      ð¿       IsInterupt        INTERUPT_ActivateSpecialEffect        HasSpecialEffectId     ´É@       @      @       GOAL_COMMON_ToTargetWarp       @       TARGET_SOUND 
       Replaning      ¡³@       FirstRoll_Flg        GOAL_COMMON_ComboRepeat      ®§@      D@       IsExistMeshOnLine        RollPathChkMiss      ¢³@       IsInsideTarget       ^@     ¸§@     ²É@    Ä   ¾ A     K¿  Ë¿  T     À  E     	 
  T AY KÁ  	¾ 
A   
Y  KÂ  	 
 E  KÃ  Y  CE 	 
     Á Y  Ä E 	T! Å  	Á 
 Ô ¾ A  	 
 ¾  
A   	A
Y 
C
 Á      Y 
ËÆ 
Y 
 
 
Ô Å  	 
 Ô KÃ Á 	Õ¾ Ô KÁ Á 	 
Y AY C	 	Á 
A	       Y   H Ô KÈ  	E 
   Ô AY C	 	Á 
A	       Y   KÁ 
 	A  
Y T
 Å  	A
 
 T É  	E 
Á
 Ô AY C	 	Á 
       Y     T Å  	A 
 Ô  ËÆ Y                    	                      GetDist        TARGET_ENE_0        GetToTargetAngle        SetStringIndexedNumber        DistMin_AAA      8@     8À       DistMax_AAA       @       BaseDir_AAA        AI_DIR_TYPE_F 
       Angle_AAA      f@       DistMin_Inter_AAA       ð?       DistMax_Inter_AAA       $@       BaseAng_Inter_AAA                Ang_Inter_AAA        AddSubGoal        GOAL_COMMON_AfterAttackAct     +   ¾ E  ¿ E  K¿   Y K¿ Á  Y K¿ A  Y K¿ Á  Y K¿ A  Y K¿ Á  Y K¿ A  Y K¿ Á  Y CE  Y           Î                          Update_Default_NoSubGoal                      F      E    Y Å   E   Y   "  I   b  I  ¢   Ç  â     "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â    "  G  b      ¢ I   â I    " I     Á Y Å     Y   b I    ¢ I   