LuaP		¶	hçõ}A       =(none)                              RegisterTableGoal $       GOAL_RedEyeGypsyDonkey321000_Battle        RedEyeGypsyDonkey321000_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate        RedEyeGypsyDonkey321000_Act01        RedEyeGypsyDonkey321000_Act02        RedEyeGypsyDonkey321000_Act20        RedEyeGypsyDonkey321000_Act21        RedEyeGypsyDonkey321000_Act22        RedEyeGypsyDonkey321000_Act23        RedEyeGypsyDonkey321000_Act24        RedEyeGypsyDonkey321000_Act25        RedEyeGypsyDonkey321000_Act26 -       RedEyeGypsyDonkey321000_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt ,       GOAL_RedEyeGypsyDonkey321000_AfterAttackAct '       RedEyeGypsyDonkey321000_AfterAttackAct            $                                      *                 '          Init_Pseudo_Global        Common_Clear_Param        GetDist        TARGET_ENE_0 
       GetHpRate        TARGET_SELF        GetRandam_Int       ğ?      Y@      .@       IsFinishTimer              V@      5@      $@      @       @      :@       SetCoolTime      §@      >@     §@       REGIST_FUNC        RedEyeGypsyDonkey321000_Act01        RedEyeGypsyDonkey321000_Act02       4@       RedEyeGypsyDonkey321000_Act20        RedEyeGypsyDonkey321000_Act21       6@       RedEyeGypsyDonkey321000_Act22       7@       RedEyeGypsyDonkey321000_Act23       8@       RedEyeGypsyDonkey321000_Act24       9@       RedEyeGypsyDonkey321000_Act25        RedEyeGypsyDonkey321000_Act26 -       RedEyeGypsyDonkey321000_ActAfter_AdjustSpace        Common_Battle_Activate              Y
  
  
  E      	Y ¿ Å  ¿ E 	À Á 
    Á 	Á 	 
   Á	ÂÔ  Ô Á 	Á 	  
 T  ÀT    A	Â  À 	  
  Á  FÀÁ 	I 	  
  A  ÂÁ 	I 	  
  Å  	I 	  
    	I 	  
    	I 	  
  Å  	I 	  
  E  	I 	  
  Å  	I 	  
  E  	I 	  
  Å  	I 	  
  	  	I 	  
  E	  		 
         Y
                           
        §@      @       GetMapHitRadius        TARGET_SELF      ÀX@               AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180        TARGET_ENE_0        GetWellSpace_Odds          ? Å  }?A A À Å 	A  
       A A YA G E                             
        §@      @       GetMapHitRadius        TARGET_SELF      ÀX@               AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180        TARGET_ENE_0        GetWellSpace_Odds          ? Å  }?A A À Å 	A  
       A A YA G E            ¤                    
       GetHpRate        TARGET_SELF ÍÌÌÌÌÌì?       AddSubGoal        GOAL_COMMON_LeaveTarget       @       TARGET_ENE_0        GetRandam_Int       $@               SetFailedEndOption -       AI_GOAL_FAILED_END_OPT__PARENT_NEXT_SUB_GOAL       0@      4@%       GOAL_COMMON_ApproachSettingDirection       ğ?      ğ¿       AI_DIR_TYPE_F 	       SetTimer       .@       GetWellSpace_Odds     8   > E  × ~ Ô K¿  A  K@ A 
  E  	  
A ÁÅ YT K¿  A  K@  
A  E  	  
A ÁÅ YK¿  Á E  Á E  	 
 E A YC A Á Y A              º                           AddSubGoal        GOAL_COMMON_Wait       ğ?       TARGET_NONE                GetWellSpace_Odds        ¾ E    Å    	 
Y  G E            Æ                           AddSubGoal         GOAL_COMMON_WalkAround_Anywhere       @      @      ğ?      ğ¿               GetWellSpace_Odds        ¾ E    Á     	A 
 A     Y  Ç Å            Ò                           GetDist        TARGET_ENE_0        GetRandam_Int        AI_DIR_TYPE_ToBL        AI_DIR_TYPE_ToBR       @       AddSubGoal %       GOAL_COMMON_ApproachSettingDirection       $@      ğ?       TARGET_SELF       ğ¿      @       GetWellSpace_Odds             %   > E  ? Å    ×¿ Ô À Å  E  	A 
   Á    Y À Å  E  	A 
  Á    Y G E            è                         ¾§@      @       GetMapHitRadius        TARGET_SELF      ÀX@               AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180        TARGET_ENE_0 	       SetTimer       .@       GetWellSpace_Odds          ? Å  }?A A À Å 	A  
       A A YË@ A 	 
Y A Ç Å            ü                    
       GetHpRate        TARGET_SELF ÍÌÌÌÌÌì?       AddSubGoal        GOAL_COMMON_LeaveTarget       @       TARGET_ENE_0        GetRandam_Int       $@               SetFailedEndOption -       AI_GOAL_FAILED_END_OPT__PARENT_NEXT_SUB_GOAL       2@      4@%       GOAL_COMMON_ApproachSettingDirection       ğ?      ğ¿       AI_DIR_TYPE_F        GetWellSpace_Odds     4   > E  × ~ Ô K¿  A  K@ A 
  E  	  
A ÁÅ YT K¿  A  K@  
A  E  	  
A ÁÅ YK¿  Á E  Á E  	 
 E A YA                                        HasSpecialEffectId        TARGET_SELF      (´@
       GetHpRate ÍÌÌÌÌÌì?       AddSubGoal #       GOAL_COMMON_LeaveTarget_Continuous       @       TARGET_ENE_0        GetRandam_Int       $@      ğ?      ğ¿       GUARD_GOAL_DESIRE_RET_Continue        @      2@      6@       SetFailedEndOption -       AI_GOAL_FAILED_END_OPT__PARENT_NEXT_SUB_GOAL %       GOAL_COMMON_ApproachSettingDirection        AI_DIR_TYPE_F        GOAL_COMMON_LeaveTarget_Escape       ø?	       SetTimer               .@       GetWellSpace_Odds     n   > E      K? E  ×  Ô Ë¿  Á  Ë@ Á 
  E  	 
 E    Y T Ë¿  Á  Ë@ Á 
  E  	  
 E     ËÂ YË¿ Å Á E  Á E  	 
  Á YÔ
 K? E  ×   Ë¿ E Á  Ë@ Á 
  E  	 
 YT Ë¿ E Á  Ë@ Á 
  E  	  
 ËÂ YË¿ Å Á E  Á E  	 
  Á YKD  A Y               1                          AddSubGoal ,       GOAL_RedEyeGypsyDonkey321000_AfterAttackAct       $@       ¾ E    Y           <                          Update_Default_NoSubGoal                              D                                     M                %          GetDist        TARGET_ENE_0        TARGET_FRI_0       @       GetMapHitRadius        TARGET_SELF        GetRandam_Int       ğ?      Y@
       GetHpRate        HasSpecialEffectId      ö³@       HasSpecialEffectAttribute        SP_EFFECT_TYPE_SLEEP        IsInterupt        INTERUPT_Damaged        ClearSubGoal               4@       AddSubGoal        GOAL_COMMON_ApproachTarget 333333ó?      ğ¿%       GOAL_COMMON_ApproachSettingDirection        AI_DIR_TYPE_F 	       SetTimer       .@     (´@#       GOAL_COMMON_LeaveTarget_Continuous       9@     A@       GUARD_GOAL_DESIRE_RET_Continue        @       SetFailedEndOption -       AI_GOAL_FAILED_END_OPT__PARENT_NEXT_SUB_GOAL        GOAL_COMMON_LeaveTarget_Escape       ø?       ¾ E  ¾   ¿ E M~À Á  	 ËÀ E 	Á E 
Á   	U Á E 
E   	U T     Â Å 
  BY   C  KC 
Á    A E    YKCÅ 
Á E Á E    Á  YËÄ A 
 Y   T Á E 
Á   Ô KC 
Á  E  À A   E    Å     ËF 
YKCÅ 
Á E Á E    Á  YËÄ A 
 Y   Ô KCÅ 
Á  E  À A   E   	 ËF 
YKCÅ 
Á E Á E    Á  YËÄ A 
 Y                                                                               Update_Default_NoSubGoal                      :      E    Y Å   E   Y   "  I   b  I  ¢   Ç  â     "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â      " I   b I    ¢ I     A Y Å     Y   â I    " I   