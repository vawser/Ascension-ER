LuaP		¶	hçõ}A       =(none)                              RegisterTableGoal        GOAL_Deer601000_Battle        Deer601000_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate        Deer601000_Act01        Deer601000_Act02        Deer601000_Act03        Deer601000_Act10        Deer601000_Act11        Deer601000_Act12        Deer601000_Act13        Deer601000_Act14        Deer601000_Act15        Deer601000_Act17         Deer601000_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt        GOAL_Deer601000_AfterAttackAct        Deer601000_AfterAttackAct            A                 	          Init_Pseudo_Global        GetStringIndexedNumber        WalkBefore        Alert_mode        TURNING_RANGE 
       Warp_Late        GetRandam_Int       ð?      Y@             YË¾   YË¾ Á  YË¾  YË¾ A YÀ Á   G           Z                 0          FearOfFire        PLAN_SIDEWAYTYPE__NONE        Common_Clear_Param        GetDist        TARGET_ENE_0        TARGET_FRI_0        GetRandam_Int       ð?      Y@       GetPrevTargetState        HasSpecialEffectId        TARGET_SELF      À@     ®¿@      6@      9@$       DeleteObserveSpecialEffectAttribute     ´É@!       AddObserveSpecialEffectAttribute      ²É@      .@     ÀW@              1@      @     A@       @      $@      D@       SetCoolTime      p§@       REGIST_FUNC        Deer601000_Act01        Deer601000_Act02        Deer601000_Act03        Deer601000_Act10       &@       Deer601000_Act11       (@       Deer601000_Act12       *@       Deer601000_Act13       ,@       Deer601000_Act14        Deer601000_Act15        Deer601000_Act17         Deer601000_ActAfter_AdjustSpace        Common_Battle_Activate     ¾         E         
  
  
        	Y K¿  K¿ E 	À Á 
  ËÀ 	 	Á 
Å   
Á  A  Á E A  À    À Á Á  À Á   Â Å A Y Ã Å Á Y Á Å Á   U T  ÉC	    T Ö Ô  W T  ÀÔ    T  Ô  W T  À Ö Ô   T  @  Ô   T  @ DT  Ä   ÉÄIBÅE      Á ÃÁ 	Å       	Å     E  	Å       	Å     Å  	Å     E	  	Å     Å	  	Å     E
  	Å     Å
  	Å       	Å     E  	Å       Å           Y          Ó                           GetRandam_Int       ð?      Y@       SetStringIndexedNumber        WalkBefore               >@       AddSubGoal        GOAL_COMMON_AttackTunableSpin       @     §@       TARGET_SELF 
       DIST_None      V@      N@#       GOAL_COMMON_ComboAttackTunableSpin      f@       GOAL_COMMON_ComboRepeat      §@       GOAL_COMMON_ComboFinal        GetWellSpace_Odds     h   > A     K?  A Y À T KÀ  A  Å 	 
A A Y Â T KÀ Å A  Å 	 
A  A A YKÀ E A  Å 	 
A A YKÀ Å A  Å 	 
A A Y KÀ Å A  Å 	 
A  A A YKÀ E A  Å 	 
A A YKÀ E A  Å 	 
A A YKÀ E A  Å 	 
A A YKÀ Å A  Å 	 
A A YA              õ                           SetStringIndexedNumber        WalkBefore                AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@     §@       TARGET_SELF 
       DIST_None      V@       GetWellSpace_Odds        > A    Y K¿  A  Å  	  
A Y                                         TARGET_ENE_0        GetDist                TARGET_FRI_0        SetStringIndexedNumber        WalkBefore        AddObserveArea        TARGET_SELF        AI_DIR_TYPE_F      v@      6@       AddSubGoal        GOAL_COMMON_AttackTunableSpin       @     §@
       DIST_None      V@       Alert_mode       ð?       GetWellSpace_Odds     %     Ë>   ?   Å  ? A   Y @   Å   	A 
 Y KÁ  A   	Å 
   Y? A  Y   Ç Å            +                	         ð?       SetStringIndexedNumber        WalkBefore        AddSubGoal         GOAL_COMMON_WalkAround_Anywhere       ð¿      $@               GetWellSpace_Odds          Ë>     Y K¿  A    	 
A Á       Y Á              A                &         @       GetMapHitRadius        TARGET_SELF        GetRelativeAngleFromTarget        TARGET_ENE_0       ð?      ð¿     v@       GetRandam_Int       Y@       ClearSubGoal        GetDist                TARGET_FRI_0        SetStringIndexedNumber        TURNING_RANGE       .@      4@      N@       AddObserveArea        AI_DIR_TYPE_F        GetStringIndexedNumber        WalkBefore        IsInsideTarget       D@       AddSubGoal        GOAL_COMMON_SpinStep       $@     p·@     q·@       AI_DIR_TYPE_B      r·@      4À     s·@       Alert_mode        GOAL_COMMON_LeaveTarget       I@       GetWellSpace_Odds     |   Ë>   Í }K?   Á @ A 	A 
  Á 	Y 	KA 	 	Á   E B 	Á @  A  Y  	Ã T KC 	      Á ËC Á Y  	ËC 	 	Õ¿ Ô KD 	    		 ËÄ 	 Á @  A       Y	Ô  T ËÄ 	 Á Á      Y	Ô F T ËÄ 	 Á A      Y	Ô ËÄ 	 Á @  A       Y	B 	  Y 	B 	  Y 	ËÄ 	Å Á   	      Y	 	G	 	E	 	 	                          $         @       GetMapHitRadius        TARGET_SELF        GetRelativeAngleFromTarget        TARGET_ENE_0                GetRandam_Int       ð?      Y@       SetStringIndexedNumber        TURNING_RANGE       .@      4@       GetDist        TARGET_FRI_0        GetStringIndexedNumber        WalkBefore       @      @      $@       @       AddSubGoal        GOAL_COMMON_LeaveTarget       ð¿       SetFailedEndOption -       AI_GOAL_FAILED_END_OPT__PARENT_NEXT_SUB_GOAL       9@     z§@     |§@       GOAL_COMMON_AttackTunableSpin        TARGET_NONE 
       DIST_None      V@     ~§@     §@       GetWellSpace_Odds     s   Ë>   Í }K?  A A @ Á 	 
  Ë@ 	 @ Á   Y  	ËA 	 	Ö¿    KB 	 	UÀ Ô  Ë@ 	 A Y 	@ 	Á A  	@ 
Á   
@  Á  @     ËÃ           Á ÄE YËA    
 Å Ô @ Á   Á  Á  ËÃ E Á   Å A  Y\ý @ A   Á   Á  ËÃ E Á   Å A  Y\ýA Ç Å            Î                         @       GetMapHitRadius        TARGET_SELF        GetRelativeAngleFromTarget        TARGET_ENE_0       ð?      ð¿     v@       GetRandam_Int       Y@       GetDist                TARGET_FRI_0       .@       GetExistMeshOnLineDistEx        AI_DIR_TYPE_F        AI_DIR_TYPE_L        AI_DIR_TYPE_R        AddSubGoal #       GOAL_COMMON_LeaveTarget_Continuous       $@      >@       GUARD_GOAL_DESIRE_RET_Continue        @       GetWellSpace_Odds     7   Ë>   Í }K?   Á @ A 	A 
  A 	 	VÁ    A 	  	Ë> 
  
A B   Å   Á @  E  Ã Å    A         Á Y Á                                 !       AddObserveSpecialEffectAttribute        TARGET_SELF     ´É@       AddSubGoal        GOAL_COMMON_ApproachTarget        @       TARGET_SOUND        GetRandam_Float       ð?      @      ð¿       GetWellSpace_Odds                > E    Y K¿  A  K@  
A  E  	  
 Y Ç Å            %                          @              Y@       Approach_Act_Flex       @     p§@       GetMapHitRadius        TARGET_SELF       ð?      ð¿      N@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     *     A  A    A      	Å  
               Y 
 
A @ Å A  KÁ     E      A  A  YA               C                          HasSpecialEffectId        TARGET_SELF      (´@       AddSubGoal #       GOAL_COMMON_LeaveTarget_Continuous       $@       TARGET_ENE_0       >@      ð?      ð¿       GUARD_GOAL_DESIRE_RET_Continue        @       GOAL_COMMON_LeaveTarget_Escape       ø?       GetWellSpace_Odds             !   > E      K¿  A  Á E  	  
A    Á Y  K¿  A  Á E  	  
A YÁ              W                          AddSubGoal        GOAL_Deer601000_AfterAttackAct       $@       ¾ E    Y           a                          Update_Default_NoSubGoal                              i                                     r                #          GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0        IsLadderAct        TARGET_SELF       9@      $@       Damaged_Act        ClearSubGoal        SetStringIndexedNumber        TURNING_RANGE       .@      4@       AddObserveArea                AI_DIR_TYPE_F      v@       GetStringIndexedNumber        AddSubGoal        GOAL_COMMON_LeaveTarget       I@      ð¿       IsInterupt        INTERUPT_ActivateSpecialEffect        HasSpecialEffectId     ´É@       @      @       GOAL_COMMON_ToTargetWarp       @       TARGET_SOUND      ²É@
       Replaning     d   ¾ A     K¿  Ë¿  T     À  E     	 
  T AY KÁ  	¾ 
A   
Y  KÂ  	 
 E  KÃ  Y  CE 	 
     Á Y  Ä E 	T	 Å  	Á 
 T ¾ A  	 
 ¾  
A   	A
Y 
C
 Á      Y 
 
 
T Å  	A 
 Ô  Ç Y                Ï    	                      GetDist        TARGET_ENE_0        GetToTargetAngle        SetStringIndexedNumber        DistMin_AAA      8@     8À       DistMax_AAA       @       BaseDir_AAA        AI_DIR_TYPE_F 
       Angle_AAA      f@       DistMin_Inter_AAA       ð?       DistMax_Inter_AAA       $@       BaseAng_Inter_AAA                Ang_Inter_AAA        AddSubGoal        GOAL_COMMON_AfterAttackAct     +   ¾ E  ¿ E  K¿   Y K¿ Á  Y K¿ A  Y K¿ Á  Y K¿ A  Y K¿ Á  Y K¿ A  Y K¿ Á  Y CE  Y                                     Update_Default_NoSubGoal                      <      E    Y Å   E   Y   "  I   b  I  ¢   Ç  â     "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â    "  G    b I    ¢ I   â I     E  Y Å   E  Y   " I    b I    