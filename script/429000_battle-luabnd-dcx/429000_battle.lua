LuaP		¶	hçõ}A       =(none)                              RegisterTableGoal        GOAL_HoundDog_429000_Battle        HoundDog_429000_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate        HoundDog_429000_Act01        HoundDog_429000_Act02        HoundDog_429000_Act03        HoundDog_429000_Act04        HoundDog_429000_Act05        HoundDog_429000_Act06        HoundDog_429000_Act07        HoundDog_429000_Act08        HoundDog_429000_Act09        HoundDog_429000_Act10        HoundDog_429000_Act11        HoundDog_429000_Act12        HoundDog_429000_Act16        HoundDog_429000_Act17        HoundDog_429000_Act18        HoundDog_429000_Act19        HoundDog_429000_Act35        HoundDog_429000_Act36 %       HoundDog_429000_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt $       GOAL_HoundDog_429000_AfterAttackAct        HoundDog_429000_AfterAttackAct            @                           EnableUnfavorableAttackCheck              p§@     r§@     v§@     x§@     §@     §@     §@     §@     §@     §@     §@     §@     §@     §@     §@     §@    A   ¾ A    Y ¾ A  Á  Y ¾ A   Y ¾ A  A Y ¾ A   Y ¾ A  Á Y ¾ A   Y ¾ A  A Y ¾ A   Y ¾ A  Á Y ¾ A   Y ¾ A  A Y ¾ A   Y ¾ A  Á Y ¾ A   Y ¾ A  A Y           [                 T          Init_Pseudo_Global        Common_Clear_Param !       AddObserveSpecialEffectAttribute        TARGET_SELF     eÊ@       GetDist        TARGET_ENE_0        GetRandam_Int       ð?      Y@       GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        HasSpecialEffectId      uÌ@     vÌ@     A@       IsInsideTarget        AI_DIR_TYPE_B       ^@      3@      4@      B@       GetTeamOrder        ORDER_TYPE_Role        ROLE_TYPE_Kankyaku       1@
       SetNumber 
       GetNumber               @       @      T@      D@       @      @      @       ROLE_TYPE_Torimaki       i@      @      >@      $@     µ@      (@     µ@      @      "@      &@      I@       SetCoolTime      p§@      .@     r§@     x§@     z§@     |§@     ~§@       REGIST_FUNC        HoundDog_429000_Act01        HoundDog_429000_Act02        HoundDog_429000_Act03        HoundDog_429000_Act04        HoundDog_429000_Act05        HoundDog_429000_Act06        HoundDog_429000_Act07        HoundDog_429000_Act08        HoundDog_429000_Act09        HoundDog_429000_Act10        HoundDog_429000_Act11        HoundDog_429000_Act12       *@       HoundDog_429000_Act13       ,@       HoundDog_429000_Act14        HoundDog_429000_Act15       0@       HoundDog_429000_Act16        HoundDog_429000_Act17       2@       HoundDog_429000_Act18        HoundDog_429000_Act19        HoundDog_429000_Act35        HoundDog_429000_Act36 +       HoundDog_419000_Act02_ActAfter_AdjustSpace        Common_Battle_Activate             Y
  
  
  E      	Y ¿ Å   	Y Ë¿  KÀ  	A 
 Á Å 
Á 	Å  A  		 Á 	Å    		T  ÉÀT+ Â 	 E  		T  Ã) ÉÀ( @ T	 Ä 	Å 	 
 Ô  Ô  Å 	  Y 	KÅ 	 	Å  Å 	  Y 	ÃIF" KÅ 	 	À Ô  Å 	  Y 	FÃCÃ @ T	 Ä 	Å 		 
 Ô  Ô  Å 	  Y 	KÅ 	 	Å  Å 	  Y 	ÃIF KÅ 	 	À Ô Å 	  Y 	FÃCÃ Â 	 E A	 		 IHIÈIÈH  ÃIHÃ Á 	Å  A
  	 
 T  É@T Á 	Å  Á
  	 
   Ô CÃEEÅEÅIHÅEIH	  Ô EÈHEÅHÈIHÅEIH   EÅHIHÃIHÅEÃET EÅEIJIÈEÅEÅC 	  
  A  À 	I 	  
  Á  ÆÆ 	I 	  
   A Ç 	I 	  
  A A È 	I 	  
   A ÆÅ 	I 	  
  Á  FÇ 	I 	  
  E  	I 	  
    	I 	  
  Å  	I 	  
    	I 	  
  E  	I 	  
    	I 	  
  Å  	I 	  
    	I 	  
  E  	I 	  
    	I 	  
  Å  	I 	  
    	I 	  
    	I 	  
    	I  	  
  E  	I 	  
  Å  	I¢ 	  
    	I 	  
    	I£ 	  
  Å  	I 	  
    	I 	  
  E  	I 	  
    	Å 
         Y
          6                          GetDist        TARGET_ENE_0       '@             8@      Y@      @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF      cÊ@      @     p§@      $@       AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180        GetWellSpace_Odds     /   > E    Á   A Á  Á  	 
Å                 Y @ E  Y Á  E  A Á  Á  Á  Â Å       Á  Á  Á  Y Á               [                          GetDist        TARGET_ENE_0       )@             8@      Y@      @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF     cÊ@      @     r§@      $@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     /   > E    Á   A Á  Á  	 
Å                 Y @ E  Y Á  E  A Á  Á  Á  Â Å       Á  Á  Á  Y Á                                         GetDist        TARGET_ENE_0       @             8@      Y@      @       Approach_Act_Flex       @     x§@      $@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     +   > E    Á   A Á  Á  	 
Å                 Y  A E   Á  Á  Á  KÁ        Á  Á  Á  Y Á  G E            ¥    "                      GetDist        TARGET_ENE_0 ffffff@             8@      Y@      @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF      dÊ@       GetRandam_Int       ð?      >@      ð¿       @       AddSubGoal        GOAL_COMMON_StepSafety       @     z§@      $@)       GOAL_COMMON_ComboTunable_SuccessAngle180        GetWellSpace_Odds     R   > E    Á   A Á  Á  	 
Å                 Y @ E  Y KA  A  ×Á       E   Á   KA  Á  Á
 T    Â E            	 	   
!Y  Á E   Á  Á  Á  Â E       Á  Á  Á  Y Á               ä                          GetDist        TARGET_ENE_0 ffffff@     8@              @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF      dÊ@      @     |§@      $@       AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180        GetWellSpace_Odds     /   > E    Á  Á    A 	 
                 Y K@  A Y  Á E      ËÁ           Y  Ç Å            	                          GetDist        TARGET_ENE_0       @             8@      Y@      @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF      eÊ@      @     §@      $@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     /   > E    Á   A Á  Á  	 
Å                 Y @ E  Y Á  E  A Á  Á  Á  Â Å       Á  Á  Á  Y Á               .                          GetDist        TARGET_ENE_0       !@             8@      Y@      @       Approach_Act_Flex       @     ~§@      $@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     +   > E    Á   A Á   	 
Å                 Y  A E   Á  Á  Á  KÁ        Á  Á  Á  Y Á  G E            U                          GetRandam_Float       ð?      @       TARGET_ENE_0        GetRandam_Int               D@     @P@       @       TARGET_SELF        GetDist       Y@      ð¿     [Ã@       AddSubGoal        GOAL_COMMON_SidewayMove        GetWellSpace_Odds     /   > A     Å  ? A A   ?  Á 	 >  	  
 E  	  
A Å  A ? A  Á      A Â Å            Y A              t                          GetDist        TARGET_ENE_0       $@             8@      Y@      @       Approach_Act_Flex       @     t§@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds     +   > E    Á   A Á   	 
Å                 Y  A E    Á  Á  Á  Á Å       Á  Á  Á  Y Á                                        @     §@       TARGET_ENE_0       $@               AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180        GetWellSpace_Odds          A    Á     	Ë¿ 
          Y 
 
Ç 
Å 
 
          °                   !       AddObserveSpecialEffectAttribute        TARGET_SELF      fÊ@      @       GetRandam_Int      §@     §@       TARGET_ENE_0       $@               AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds        > E    Y Á  ? A   Å  A A A 	Á 
Å       A A A Y 
A 
 
 
 
          Æ                         @     §@       TARGET_ENE_0       $@               AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180        GetWellSpace_Odds          A    Á     	Ë¿ 
          Y 
 
Ç 
Å 
 
          Û                          GetRandam_Int       @      @       TARGET_ENE_0               ð?      >@     F@       @       TARGET_SELF        GetDist       Y@      ð¿     [Ã@!       AddObserveSpecialEffectAttribute      ¢³@       AddSubGoal        GOAL_COMMON_SidewayMove       @     Q@      I@     r·@     s·@#       GOAL_COMMON_ComboAttackTunableSpin      p·@       GetWellSpace_Odds     d   > A     Å  >  A  >  Á 	  E  	A 
Å  
 > A Á   ×   A B E Á Y Â E         YC Ô WC T C    > A   Å      B E Á Y Â Å          Y  ?     Å      B E Á Y Â Å          Y  G E            3                          @       TARGET_ENE_0      F@       GUARD_GOAL_DESIRE_RET_Continue                GetRandam_Int       ð?      Y@      ð¿     [Ã@       AddSubGoal        GOAL_COMMON_Turn        GetWellSpace_Odds          E    Å    Ë? 	 Á  	 
   A 
Á Å          Y              O                          AddSubGoal        GOAL_COMMON_Turn        @       TARGET_ENE_0      V@               GetWellSpace_Odds        ¾ E    Å   A 	A 
Y A              W                
         ð?      ð¿       TARGET_ENE_0       @               GetRandam_Int        @       AddSubGoal        GOAL_COMMON_StepSafety        GetWellSpace_Odds     "     A  A        Á  	 
 Ë?     > T    A  KÀ               Y  G E            t                          GetDist        TARGET_ENE_0       $@    ÀÓ@      @       GetMapHitRadius        TARGET_SELF                AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        GetWellSpace_Odds        > E    Á  Ë?  Á Á À 	E    E       Á Á Y	Á 	 	 	 	                                    GetDist        TARGET_ENE_0       )@             8@      Y@      @       Approach_Act_Flex $       DeleteObserveSpecialEffectAttribute        TARGET_SELF     cÊ@    dÊ@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin       $@     r§@     v@       GOAL_COMMON_ComboRepeat      §@     ¸§@       GetWellSpace_Odds     C   > E    Á   A Á  Á  	 
Å                 Y @ E  Y @ E Á Y Á E  Á E   Á   Á  Á  YÁ E   E   Á  Á  Á  Á  YÁ E  Á E   Á  Á  Á  Á  YÁ               ¦                          AddSubGoal $       GOAL_HoundDog_429000_AfterAttackAct       $@       ¾ E    Y           ­                          Update_Default_NoSubGoal                              ´                                     Ò    !            ?          IsInterupt        INTERUPT_ActivateSpecialEffect        HasSpecialEffectId        TARGET_SELF      cÊ@$       DeleteObserveSpecialEffectAttribute        GetDist        TARGET_ENE_0        GetRandam_Int       ð?      Y@       ClearSubGoal       @      $@      @     t§@               AddSubGoal        GOAL_COMMON_ComboRepeat     cÊ@333333@     §@       @      D@     §@!       AddObserveSpecialEffectAttribute      eÊ@(       GOAL_COMMON_ComboRepeat_SuccessAngle180      §@     §@     fÊ@     dÊ@     Q@      N@     ~§@    dÊ@@     §@     §@     §@     v§@      @      >@    eÊ@       IsFinishTimer 	       SetTimer        GetRandam_Float       @      @
       GetNumber 
       SetNumber        @ffffffþ?333333@      @     z§@     |§@#       GOAL_COMMON_ComboAttackTunableSpin       ð¿       GOAL_COMMON_StepSafety       T@       INTERUPT_Shoot        HoundDog_429000_Act19       ¾ E  À ¿ Å    T Ë¿ Å   Y À Å À A   KAY ×   ×Á   Á Å   	 
 ËB          Y ¿ Å  Á  T Ë¿ Å  Á Y À Å À A   KAY Ã T  A Å   	 
 ËB          Y  Ä  À A   WD   Á  Å 	 
   ËÄ Å   Y ËB          Y ËBÅ           Y Ô  À  	A 
 Å  	 
  ËÄ Å   Y ËB          Y ¿ Å  Á   Ë¿ Å  Á Y À Å À A   KAY ×  	 F Ô ËÄ Å   Y  Å    	 
À A   ×F T    À  A   ËB         Y   A Å   	 
 ËÄ Å  Á Y ËB          Y ¿ Å  Á  * Ë¿ Å  Á Y À Å À A   KAY Ç T F   A	 	 Å  	 
  F T ËB          Y ËB         Y   Á	 
 Å  	 
  ËB          Y ËB         Y T ×È   Á	 
 Å  	 
  ËB          Y ËB         Y  Ä  À A   É   A	 	 Å 	 
   I T ËB          Y ËB           Y Ô ËÄ Å   	Y  À  	A 
 Å  	 
  ËB          Y ¿ Å     Ë¿ Å   Y À Å À A   KAY Ç   A	 	 Å  	 
  F T ËB          Y ËB         Y  Ä  À A   É   A	 	 Å 	 
   I T ËB          Y ËB           Y Ô ËÄ Å   	Y  À  	A 
 Å  	 
  ËB          Y ¿ Å  Á
  T* À Å À A   ËÄ Å  Á Y É    ËÉ  Ê 	Á   	Y  ËÊ  B  Ë  A 	Y  ËÊ  Õ@  Ë  Á 	Y  ËÊ  UK  Ë   	Y 
 ËÊ  A T	 Ë   	Y  É    Õ  ËÊ  B T   Ô ËÊ  Õ@ T  A  ËÊ  UK T   T ËÊ  A   A W  KAY F   À Á 	 
 Å A 	 
  ËBE          Y T    A 	A 
Å    À A Á  ÕÀ T  A 
 	ËBÅ               Y  Á Å A    ËBE      	 	    Y ¿ Å    Ô À Å À A   ËÄ Å  Á Y Â  KAY M Ô  Á Å A ËB	Å       Y	
    A A 	Å 
   À A Á  Õ@ T  A 	 ËBÅ              Y  Á Å A    ËBÅ       	Y  ¾ E  À Å À A   KAY      Y               È                                                               Update_Default_NoSubGoal                      L      E    Y Å   E   Y   "  I   b  I  ¢   Ç  â     "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â    "  G    b I    ¢ I   â I     E  Y Å   E  Y   " I    b I    