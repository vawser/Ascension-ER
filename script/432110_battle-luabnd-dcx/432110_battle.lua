LuaP		Ά	hηυ}A       =(none)                              RegisterTableGoal ,       GOAL_RoamLowSoldierChildShotel432110_Battle '       RoamLowSoldierChildShotel432110_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate %       RoamLowSoldierChildShotel432110_Act1 %       RoamLowSoldierChildShotel432110_Act2 %       RoamLowSoldierChildShotel432110_Act3 %       RoamLowSoldierChildShotel432110_Act4 %       RoamLowSoldierChildShotel432110_Act5 %       RoamLowSoldierChildShotel432110_Act6 %       RoamLowSoldierChildShotel432110_Act7 %       RoamLowSoldierChildShotel432110_Act8 %       RoamLowSoldierChildShotel432110_Act9 '       RoamLowSoldierChildHatchet432110_Act10 '       RoamLowSoldierChildHatchet432110_Act15 &       RoamLowSoldierChildShotel432110_Act30 &       RoamLowSoldierChildShotel432110_Act31 &       RoamLowSoldierChildShotel432110_Act32 &       RoamLowSoldierChildShotel432110_Act33 5       RoamLowSoldierChildShotel432110_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt 4       GOAL_RoamLowSoldierChildShotel432110_AfterAttackAct /       RoamLowSoldierChildShotel432110_AfterAttackAct            6                    
       SetNumber       π?               EnableUnfavorableAttackCheck      p§@     r§@     t§@     v§@     x§@     §@     §@     §@     §@     §@     §@    1   Ύ A    Y KΏ    Y KΏ   A Y KΏ    Y KΏ   Α Y KΏ    Y KΏ   A Y KΏ    Y KΏ   Α Y KΏ    Y KΏ   A Y KΏ    Y           i                 P          Common_Clear_Param !       AddObserveSpecialEffectAttribute        TARGET_ENE_0      ΐT@     V@     P»@       GetDist 	       GetDistY 
       GetHpRate        TARGET_SELF        GetRandam_Int       π?      Y@               GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        HasSpecialEffectId     aΗ@    cΗ@     fΗ@    fΗ@
       GetNumber       @       GetTeamOrder        ORDER_TYPE_Role        ROLE_TYPE_Kankyaku       @      @      N@       @      D@      "@     @@      >@       ROLE_TYPE_Torimaki       $@      4@       GetLatestSoundBehaviorID     _A    _A      .@      @       @      @       InsideRange       ^@     ΐX@      9@      n@      I@       SetCoolTime      §@     §@     §@     §@     §@     Ά§@     ¬§@
       SetNumber        PLAN_SP_EFFECT_BUDDY_DECLARE        REGIST_FUNC %       RoamLowSoldierChildShotel432110_Act1 %       RoamLowSoldierChildShotel432110_Act2 %       RoamLowSoldierChildShotel432110_Act3 %       RoamLowSoldierChildShotel432110_Act4 %       RoamLowSoldierChildShotel432110_Act5 %       RoamLowSoldierChildShotel432110_Act6 %       RoamLowSoldierChildShotel432110_Act7 %       RoamLowSoldierChildShotel432110_Act8 %       RoamLowSoldierChildShotel432110_Act9 '       RoamLowSoldierChildHatchet432110_Act10 '       RoamLowSoldierChildHatchet432110_Act15 &       RoamLowSoldierChildShotel432110_Act30       ?@&       RoamLowSoldierChildShotel432110_Act31       @@&       RoamLowSoldierChildShotel432110_Act32 &       RoamLowSoldierChildShotel432110_Act33 5       RoamLowSoldierChildShotel432110_ActAfter_AdjustSpace        Common_Battle_Activate       
  
  
        	Y ΛΎ   Α  	Y ΛΎ    	Y ΛΎ   A 	Y ΐ   Kΐ   	ΐ E 
Α 	Α   	A 
Β Ε Β E A  Β E   Β E Α  Β E      ΛΓ Α UAT  A    ΛΓ Α UAT  A UΑ T KΔ  E U Τ   Ε	Ζ	ΖAT ΙΖ	Ζ	ΖΕ UΑ Τ KΔ   U T  T Ε	Ζ	ΖΗA ΙΖ	Ζ	ΖΗΕ  Τ ΛΗ  HΤ  ΛΗ  UH Τ   Ε	Ζ	Ζ	ΖEA ΙΖ	Ζ	Ζ	ΖΙFΕΤ   ΙΘIIIΑΙAΙΑΙΘΙΘΙH	      A A A   Τ ΗIΚH	Ζ	FΙΖ	F      A  A   T ΘIΗEHΙΚ  ΙΖΙΖ	F     Α A
 FΑΑ 	      A
 FΑΑ 	     A A
 ΖΘΑ 	      
 FΕΑ 	     Α 
 FΕΑ 	      A FΗΑ 	     A 
 ΘΑ 	   ΙΑ Τ ΛΗ  HΤ  ΛΗ  UH  ΙΑΙAΙΑΙAT ΙΑΙΑΝ  A Y ΛΓ  UA T  ΙΑT ΛΓ  ΥA   ΙΑΒ E Ε   U T  ΙΑ  ΙA  T  ΙΑ  ΙΑ     E  	       	     Ε  	       	     E  	       	     Ε  	       	     E  	       	     Ε  	       	       	‘       	’     E  	       Ε           Y          i                         @       GetMapHitRadius        TARGET_SELF               Y@       @      @       Approach_Act_Flex        HasSpecialEffectId     cΗ@     §@     §@      @       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     @   Λ>   Ν }LΏLΏ Α  A  	Ε 
               Y 
@ 
  A  
 Α Λ>   MΑ  Α    Τ ΛΑ     Ε     Α  Α  Y ΛΑ    Ε     Α  Α  YΑ                                        @       GetMapHitRadius        TARGET_SELF               Y@       @      @       Approach_Act_Flex      §@      @       GetRandam_Int       π?      N@       IsInsideTargetCustom        TARGET_ENE_0        AI_DIR_TYPE_R      f@     V@     ΐX@       AddSubGoal        GOAL_COMMON_SpinStep      r·@       AI_DIR_TYPE_L      s·@#       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     O   Λ>   Ν }LΏLΏ Α  A  	Ε 
               Y 
 
Λ>   ΝΑ  Α  A Α   A  ΛA    Ε  A   T KΓ  A A  Α   Α  Y KΓ  A Α  Α  Ε Α  YKΓ  A        Α  Α  YΑ  G E            Ή                         @       GetMapHitRadius        TARGET_SELF               Y@       @      @       Approach_Act_Flex      §@      @       GetRandam_Int       π?      N@       IsInsideTargetCustom        TARGET_ENE_0        AI_DIR_TYPE_R      f@     V@     ΐX@       AddSubGoal        GOAL_COMMON_SpinStep      r·@       AI_DIR_TYPE_L      s·@#       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     O   Λ>   Ν }LΏLΏ Α  A  	Ε 
               Y 
 
Λ>   ΝΑ  Α  A Α   A  ΛA    Ε  A   T KΓ  A A  Α   Α  Y KΓ  A Α  Α  Ε Α  YKΓ  A        Α  Α  YΑ  G E            ΰ                         @       GetMapHitRadius        TARGET_SELF               Y@       @      @       Approach_Act_Flex      §@      @       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     ,   Λ>   Ν }LΏLΏ Α  A  	Ε 
               Y 
 
Λ>   ΝΑ  Α  Α Ε A        Α  Α  YΑ  G E            ό                         @       GetMapHitRadius        TARGET_SELF               Y@       @      @       Approach_Act_Flex      §@      @       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     ,   Λ>   Ν }LΏLΏ Α  A  	Ε 
               Y 
 
Λ>   ΝΑ  Α  Α Ε A        Α  Α  YΑ  G E                               
       SetNumber       π?      $@              Y@       @      @       Approach_Act_Flex        GetDist        TARGET_ENE_0      §@      @       GetMapHitRadius        TARGET_SELF        AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     0   > A  A  Y   LΏLΏ Α  A  	Ε 
               Y 
@ 
E 
 A E Α  Α  Β Ε Α  E      Α  Α  YΑ               :                         @       GetMapHitRadius        TARGET_SELF               Y@       @      @       Approach_Act_Flex        HasSpecialEffectId     cΗ@     §@     §@      @       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     @   Λ>   Ν }LΏLΏ Α  A  	Ε 
               Y 
@ 
  A  
 Α Λ>   MΑ  Α    Τ ΛΑ     Ε     Α  Α  Y ΛΑ    Ε     Α  Α  YΑ               Z                          GetRandam_Int       π?      Y@
       SetNumber       @     @U@       AddSubGoal        GOAL_COMMON_ApproachAround        TARGET_ENE_0                TARGET_SELF       πΏ       AI_DIR_TYPE_ToBL       @      $@     Q@       AI_DIR_TYPE_ToBR      A@       AI_DIR_TYPE_ToL        @      (@       AI_DIR_TYPE_ToR        GetWellSpace_Odds     Z   > A     K?  A  Y Φ T ΐ Ε > A  	 
  A 	 
  Α  > A   Y   Φ T ΐ Ε > A  	 
  A 	 
  Α  > A   Y  	 Φ T ΐ Ε > A  	 
  A 	 
  Α  > Α   Y   ΐ Ε > A  	 
  A 	 
  Α E > Α   Y  A              u                          GetRandam_Int       π?      Y@
       SetNumber       @             @P@      @       GetMapHitRadius        TARGET_SELF        @       Approach_Act_Flex        HasSpecialEffectId     cΗ@     §@     §@      @       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0      A@      @     §@      @     §@     §@       GetWellSpace_Odds     ΄   > A     K?  A Y Φ  Τ @ E Μ?Μ?  A  	 
Ε                 Y A E A   Α @ E A A  U Τ ΛΒ    Ε      A A Y ΛΒ     Ε      A A Y Φ  Τ
 @ E Μ?Μ?  A  	 
Ε                 Y  @ E A A > A     ΛΒ    Ε      A A Y @ E Μ?Μ?  A  	 
Ε                 Y A E A   A @ E A A  U Τ ΛΒ    Ε      A A Y ΛΒ     Ε      A A YA              Θ                   
       SetNumber       π?       GetDist        TARGET_ENE_0       $@       GetMapHitRadius        TARGET_SELF               Y@       @      @       Approach_Act_Flex        AddSubGoal        GOAL_COMMON_SpinStep       @     q·@       AI_DIR_TYPE_B      Ά§@      N@#       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     A   > A  A  Y ? Ε  Λ?  L@L@ Α A 	 
Ε                 Y Χΐ  Α E  Α Ε  Α  Α Y? Ε  A Λ?  MA  Α Ε    Ε      Α Α YΑ              ξ                         $@              Y@       @      @       Approach_Act_Flex        GetDist        TARGET_ENE_0      ¬§@      @       GetMapHitRadius        TARGET_SELF        AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     ,     ΜΎΜΎ  A  Α   	E 
               Y 
@ 
Ε 
 A Ε A  A  Α E A  Ε      A  A  YA                                         AddSubGoal        GOAL_COMMON_SidewayMove        GetRandam_Float        @      @       TARGET_ENE_0        GetRandam_Int               π?      >@     F@      πΏ       GetWellSpace_Odds        Ύ E  ? Α   	 E @ Α 
  @ 	A   	 
 Α Y Α                                        IsInsideTargetCustom        TARGET_SELF        TARGET_ENE_0        AI_DIR_TYPE_R      f@     V@     ΐX@       AddSubGoal        GOAL_COMMON_SpinStep       @     r·@               AI_DIR_TYPE_L      s·@       GetWellSpace_Odds     "   > E    Ε   A 	 
 T Kΐ  A    Α 	 
Α Y Kΐ  A A   Α 	Ε  
Α YΑ              -                          AddSubGoal        GOAL_COMMON_SpinStep       @     q·@       TARGET_ENE_0                AI_DIR_TYPE_B        GetWellSpace_Odds        Ύ E    Α   A 	 
A YA Η Ε            9                          GetDist        TARGET_ENE_0        GetRandam_Float        @      @      @      @      π?      πΏ      @       AddSubGoal        GOAL_COMMON_ApproachTarget        TARGET_SELF        GetWellSpace_Odds             &   > E  ? Α    ? A    Χ T Α Ε 	  
E        Y Α Ε 	  
E       Y G E            P                          AddSubGoal 4       GOAL_RoamLowSoldierChildShotel432110_AfterAttackAct       $@       Ύ E    Y           [                          Update_Default_NoSubGoal                              c                                     l                          GetDist        TARGET_ENE_0       @       GetMapHitRadius        TARGET_SELF        GetRandam_Int       π?      Y@
       GetHpRate        HasSpecialEffectId      φ³@       HasSpecialEffectAttribute        SP_EFFECT_TYPE_SLEEP        IsInterupt        INTERUPT_ActivateSpecialEffect $       GetSpecialEffectActivateInterruptId      ΐT@     V@     P»@       SP_EFFECT_TYPE_POIZON        ClearSubGoal %       RoamLowSoldierChildShotel432110_Act6 %       RoamLowSoldierChildShotel432110_Act7     [   Ύ E  KΏ  ~ΛΏ  Α  ΐ  Λΐ  	 
   KΑ  	 
   T     ΛΑ  		 KΒ  	XT KΒ A 	X KΒ  	Τ KΑ E  	Ε 
     CY E     	Y  Τ CY      	Y  ΛΑ  	 KΒ  	Τ  CY                Ή                                     Ύ                          Update_Default_NoSubGoal                      F      E    Y Ε   E   Y   "  I   b  I  ’   Η  β     "  G  b    ’  Η  β    "  G  b    ’  Η  β    "  G  b    ’  Η  β    "  G  b      ’ I   β I    " I     Α Y Ε     Y   b I    ’ I   