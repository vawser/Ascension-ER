LuaP		¶	hçõ}A       =(none)                              RegisterTableGoal '       GOAL_GhoulChildrenScepter395020_Battle "       GhoulChildrenScepter395020_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate !       GhoulChildrenScepter395020_Act01 !       GhoulChildrenScepter395020_Act02 !       GhoulChildrenScepter395020_Act03 !       GhoulChildrenScepter395020_Act40 !       GhoulChildrenScepter395020_Act41 !       GhoulChildrenScepter395020_Act42 !       GhoulChildrenScepter395020_Act43 !       GhoulChildrenScepter395020_Act44 !       GhoulChildrenScepter395020_Act45 !       GhoulChildrenScepter395020_Act46 !       GhoulChildrenScepter395020_Act49 0       GhoulChildrenScepter395020_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt /       GOAL_GhoulChildrenScepter395020_AfterAttackAct *       GhoulChildrenScepter395020_AfterAttackAct            +                                      1                 C          Init_Pseudo_Global        SetStringIndexedNumber        Dist_SideStep       @       Dist_BackStep        GetStringIndexedNumber        MagicLoop_Cnt        ForceGreatMagic_Flg        Common_Clear_Param        GetDist        TARGET_ENE_0        GetRandam_Int       ð?      Y@       GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        GetEventRequest $       DeleteObserveSpecialEffectAttribute        TARGET_SELF      ¡³@     ¢³@     £³@     ¤³@       GetTeamOrder        ORDER_TYPE_Role        ROLE_TYPE_Kankyaku      H@       ROLE_TYPE_Torimaki       6@      $@       @      4@     Q@       IsInsideTargetCustom        AI_DIR_TYPE_F      k@      ð¿      D@       GetMapHitRadius       >@      N@     D@              @      T@      @       @      E@      G@     V@       REGIST_FUNC !       GhoulChildrenScepter395020_Act01 !       GhoulChildrenScepter395020_Act02 !       GhoulChildrenScepter395020_Act03 !       GhoulChildrenScepter395020_Act40 !       GhoulChildrenScepter395020_Act41 !       GhoulChildrenScepter395020_Act42      E@!       GhoulChildrenScepter395020_Act43       F@!       GhoulChildrenScepter395020_Act44      F@!       GhoulChildrenScepter395020_Act45 !       GhoulChildrenScepter395020_Act46 !       GhoulChildrenScepter395020_Act49 0       GhoulChildrenScepter395020_ActAfter_AdjustSpace        Common_Battle_Activate     ã         YË¾   Á  Y Ë¾  Á  Y Ë¿  YË¿ Á Y
  
  
       	Y ËÀ  KÁ  	A 
 Â Å 
Â 	 	ËÂ 
 Á Y 
ËÂ 
  Y 
ËÂ 
 A Y 
ËÂ 
  Y 
A Ô KÄ 
 
E Õ T  ÉA A Ô KÄ 
 
Å Õ T T  ÖE T  ÉA ÉEIFF ËÆ 
   Á 	 È  L 
 
T  T Å 
A T  IH IHH	ÉÉEÔ	  T Å 
A T  IH HÉE	ÉIFÔ   Å 
A T  IH I	I	É	ÉIF Å 
A   
 
Ç 
 ÉIFT J   ÉÅÉJ  ÉÁ 
    Å  
 
      
 
    E  
 
      
 
    Å  
 
      
 
      
 
      
 
      
 
    Å  
 
      
 
    E  
           Y          ß                          >@              Y@       @       Approach_Act_Flex        MagicLoop_Cnt !       AddObserveSpecialEffectAttribute        TARGET_SELF      ¡³@     ¢³@     £³@      @     p§@      @       GetMapHitRadius       ø?      N@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     8     A  A    A  Á  Á  	 
               Y 
A  
G 
@ 
Å  Y 
@ 
Å A Y 
@ 
Å  Y 
Á 
 B Å Á  ËÂ     Å      A  A  YA                                        D@              Y@       @       Approach_Act_Flex        ForceGreatMagic_Flg !       AddObserveSpecialEffectAttribute        TARGET_SELF      ¡³@     ¢³@      @     x§@      @       GetMapHitRadius       ø?      N@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     4     A  A    A  Á  Á  	 
               Y 
A  
G 
@ 
Å  Y 
@ 
Å A Y 
 
Á ËA Å  Á Â E          A  A  YA  Ç Å            "                         @              Y@       @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF      ¡³@     ¢³@     ¤³@      @     v§@       GetMapHitRadius        AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin        TARGET_ENE_0        GetWellSpace_Odds     6     A  A    A  Á  Á  	 
               Y 
Ë? 
 Á Y 
Ë? 
  Y 
Ë? 
 A Y 
 
Á A  A  A  ËÁ     Å      A  A  YA               D                
          @      9@      ð?      ð¿       AddSubGoal        GOAL_COMMON_ApproachTarget        TARGET_ENE_0        TARGET_SELF        GetWellSpace_Odds                  A   Á  ¿ E 	 
   Å    YA              Z                
          @      9@      ð?      ð¿       AddSubGoal        GOAL_COMMON_ApproachTarget        TARGET_ENE_0        TARGET_SELF        GetWellSpace_Odds                  A    Á  ¿ E 	 
   Å    YA              m                	          AddSubGoal        GOAL_COMMON_Turn        @       TARGET_ENE_0        GetRandam_Int       .@      4@               GetWellSpace_Odds        ¾ E    Å  ? A 
  Á 	Á 
Y Á              {                	         ð?              Y@       TARGET_ENE_0       ð¿       AddSubGoal        GOAL_COMMON_StepSafety        GetDist        GetWellSpace_Odds          A    A  A  Å    	 
 Ë¿               Y K@ Å  A                                         GetRandam_Int               ð?       @       TARGET_ENE_0       .@      ð¿       GUARD_GOAL_DESIRE_RET_Failed        AddSubGoal        GOAL_COMMON_SidewayMove        isLifeSuccess        GetWellSpace_Odds        > A     Á    A   	Å 
 À E             YA  Ç Å            ®                          GetRandam_Int               ð?      @       TARGET_ENE_0       $@      ð¿       GUARD_GOAL_DESIRE_RET_Failed        @       AddSubGoal !       GOAL_COMMON_LeaveTargetToPathEnd        GetWellSpace_Odds        > A     Á   A    	Å 
   ËÀ                Y A  Ç Å            Ç                         @      Y@      ð?      ð¿       TARGET_ENE_0                AddSubGoal        GOAL_COMMON_SpinStep      p·@       AI_DIR_TYPE_F        GetWellSpace_Odds          A  Á  Á  Á     	A 
  À Å     A E A YA              Ü                         $@      6@      ð?      ð¿      ø?       @       IsExistMeshOnLine        TARGET_SELF        AI_DIR_TYPE_R        AI_DIR_TYPE_L        AI_DIR_TYPE_F        AI_DIR_TYPE_B        GetDist        TARGET_ENE_0        GetRandam_Int                AddSubGoal        GOAL_COMMON_ApproachTarget        GetRandam_Float        GetWellSpace_Odds        GOAL_COMMON_SidewayMove       Y@       resultTypeIfGuardSuccess        GOAL_COMMON_Wait       à?       GOAL_COMMON_LeaveTarget        GUARD_GOAL_DESIRE_RET_Success          A  Á        	A 
@ Å   @ Å E  @ Å   @ Å Å  A E B Á     U Ô   U     U    U T  Á    U   U T       U Ô    U   A Ö  Â E   E C     Å    YÁ Ç Å  T  T × Ô ? Ô Â   E   A       Y Â Å  E YÁ Ç Å  T	 Ö Ô  U T Â E   E C     E     Y  ? Ô Â   E   A       Y Â Å  E YÁ Ç Å            `                          AddSubGoal /       GOAL_GhoulChildrenScepter395020_AfterAttackAct       $@       ¾ E    Y           k                          Update_Default_NoSubGoal                              s                                     |                "          IsLadderAct        TARGET_SELF       @       GetMapHitRadius               4@       GetDist        TARGET_ENE_0        GetRandam_Int       ð?      Y@       IsInterupt        INTERUPT_ActivateSpecialEffect        HasSpecialEffectId      ¢³@       MagicLoop_Cnt       @       IsInsideTargetCustom        AI_DIR_TYPE_F      V@      ð¿      D@       ClearSubGoal        AddSubGoal        GOAL_COMMON_ComboRepeat ù?     r§@       ForceGreatMagic_Flg      £³@     t§@     ¤³@     k@      @     z§@    ¤   ¾ E  T     K¿ E  Í ~ A À Å À A 	 
 KÁ  
 T" ËÁ E  
    Å Ì@Ç B      T ËÂ E  
Å  Á  A    Å ? Ô DY KD 
A  Å      Y   Å ~ T A Ç DY  ËÁ E  
    Å Ì@Ç B       ËÂ E  
Å  Á  A    Å ? Ô DY KD 
A A Å      Y  T
 Å ~ 	 A Ç DY T ËÁ E  
   Ô ËÂ E  
Å  Á  K¿ E  Ì   DY KD 
 A Å      Y               Þ                          Update_Default_NoSubGoal                      ;      E    Y Å   E   Y   "  I   b  I  ¢   Ç  â     "  G  b    ¢  Ç  â    "  G  b    ¢  Ç  â    "  G  b      ¢ I   â I    " I     Á Y Å     Y   b I   