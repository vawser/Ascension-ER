LuaP		¶	hçõ}A       =(none)                              RegisterTableGoal (       GOAL_DosouSkeletonCrossbow350010_Battle #       DosouSkeletonCrossbow350010_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate "       DosouSkeletonCrossbow350010_Act01 "       DosouSkeletonCrossbow350010_Act02 "       DosouSkeletonCrossbow350010_Act03 "       DosouSkeletonCrossbow350010_Act04 "       DosouSkeletonCrossbow350010_Act05 "       DosouSkeletonCrossbow350010_Act15 "       DosouSkeletonCrossbow350010_Act30 "       DosouSkeletonCrossbow350010_Act31 1       DosouSkeletonCrossbow350010_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt 0       GOAL_DosouSkeletonCrossbow350010_AfterAttackAct +       DosouSkeletonCrossbow350010_AfterAttackAct            &                                      ,                 0          Init_Pseudo_Global        Common_Clear_Param $       DeleteObserveSpecialEffectAttribute        TARGET_SELF      ¡³@       HasSpecialEffectId     {È@       GetDist        TARGET_ENE_0        GetRandam_Int       ð?      Y@       GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer     È@      .@       InsideRange      f@     Àb@             ÀX@       @      @      >@      @     V@       GetTeamOrder        ORDER_TYPE_Role        ROLE_TYPE_Kankyaku       ?@       ROLE_TYPE_Torimaki      Q@      D@       SetCoolTime      ¢§@     ¬§@       REGIST_FUNC "       DosouSkeletonCrossbow350010_Act01 "       DosouSkeletonCrossbow350010_Act02 "       DosouSkeletonCrossbow350010_Act03       @"       DosouSkeletonCrossbow350010_Act04 "       DosouSkeletonCrossbow350010_Act05 "       DosouSkeletonCrossbow350010_Act15 "       DosouSkeletonCrossbow350010_Act30 "       DosouSkeletonCrossbow350010_Act31 1       DosouSkeletonCrossbow350010_ActAfter_AdjustSpace        Common_Battle_Activate     ô         Y
  
  
  E      	Y ¿ Å   	Y Ë¿ Å   	 KÀ  	ËÀ  
Á  Á 	E 	Ë¿ 
Å    
 Õ  × T      A  Á  T  IÁ ID Ö T      A  Á  T  IÁ ID      A  Á  T  IÁ IDÉDÔ Á Ô Å Å   T × T  IÁÔ IÁT Á  Å Å    × T  IÁT IDIÆ × T      A  Á  T  IÁ IA Ö T      A  Á  T  IÁ IA      A  Á  T  IÁ  IDÉDÆE       ÄÁ ÉE     Á Á FÂÁ É  Õ   IÃ	     E	  É	     	  É	     Å	  É	     E
  É	     
  É	     Å
  É	       É	     E  É	       Å          Y          Ò                         4@       GetMapHitRadius        TARGET_SELF               I@      @       @       Approach_Act_Flex      §@     §@      @       GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0 !       AddObserveSpecialEffectAttribute      ¡³@      ø?       AddSubGoal        GOAL_COMMON_LeaveTarget       @       @      ð¿#       GOAL_COMMON_ComboAttackTunableSpin       $@       GetWellSpace_Odds     H   Ë>   Í }L¿¿ Á  A  	Å 
               Y 
 
A Ë>   Ë>   MÁÁ  Á  KA  A  B Å B   A Y Ã  KÃ  A Å  Å   Á YKÃ  A   Å     Á  Á  YÁ               ÿ     	                      AddSubGoal        GOAL_COMMON_Turn       à?       TARGET_ENE_0                GetWellSpace_Odds        ¾ E    Å   Y  G E                                    ¢§@      @       GetMapHitRadius        TARGET_SELF                GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0 !       AddObserveSpecialEffectAttribute      ¡³@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin       $@       AppDist        GetWellSpace_Odds     '     ? Å  }? Å  M}Ì¾  Ë?  
Á  @ 	E 	A 
Å  Á Y 
Á 
E   E Å      Y
 
 
 
 
          -                        ¤§@      @       GetMapHitRadius        TARGET_SELF                GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0 !       AddObserveSpecialEffectAttribute      ¡³@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin       $@       AppDist        GetWellSpace_Odds     '     ? Å  }? Å  M}Ì¾  Ë?  
Á  @ 	E 	A 
Å  Á Y 
Á 
E   E Å      Y
 
 
 
 
          O                        §@     §@      @       GetMapHitRadius        TARGET_SELF                GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0 !       AddObserveSpecialEffectAttribute      ¡³@      ø?       AddSubGoal        GOAL_COMMON_LeaveTarget       @       @      ð¿#       GOAL_COMMON_ComboAttackTunableSpin       $@       AppDist        GetWellSpace_Odds     3     A  K?  M~K?  ~?A A @ 	Á   	Ë@ 
 
KA   Y ×A  Â Å   A     YÂ Å    E    A A YA                                       *@              I@      Y@      @       @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF     0Ñ@     ¬§@      @       GetRandam_Int       ð?       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin       $@       TARGET_ENE_0        GetWellSpace_Odds     /     Ì¾¿Á  A   A 	 
               Y 
K@ 
 A Y 
 
Á Á A  A  A A Á   Â Å    E     A  A  YA               ¢                          AddSubGoal        GOAL_COMMON_SidewayMove        GetRandam_Float        @      @       TARGET_ENE_0        GetRandam_Int               ð?      >@     F@      ð¿       GetWellSpace_Odds        ¾ E  ? Á   	 E @ Á 
  @ 	A   	 
 Á Y Á              °                          GetDist        TARGET_ENE_0        GetRandam_Float        @      @      "@      ,@      ð?      ð¿       AddSubGoal        GOAL_COMMON_ApproachTarget        TARGET_SELF        GetWellSpace_Odds                > E  ? Á    ? A    ËÀ  	  
E   Å    YA              Ê                          AddSubGoal 0       GOAL_DosouSkeletonCrossbow350010_AfterAttackAct       $@       ¾ E    Y           Õ                          Update_Default_NoSubGoal                              Ý                                     æ                          GetDist        TARGET_ENE_0       @       GetMapHitRadius        TARGET_SELF        GetRandam_Int       ð?      Y@
       GetHpRate        HasSpecialEffectId      ö³@       HasSpecialEffectAttribute        SP_EFFECT_TYPE_SLEEP        IsInterupt        INTERUPT_ActivateSpecialEffect $       GetSpecialEffectActivateInterruptId      ¡³@       IsInsideTargetCustom        AI_DIR_TYPE_F      v@     f@      ø?       ClearSubGoal        AddSubGoal        GOAL_COMMON_ComboFinal       $@     §@     V@    F   ¾ E  K¿  ~Ë¿  Á  À  ËÀ  	 
   KÁ  	 
   T     ËÁ  	Ô KÂ  	 ËÂ  	E  
 Á  A   DY   Ô DY KD 	A 
 E    Á Y                                                                               Update_Default_NoSubGoal                      8      E    Y Å   E   Y   "  I   b  I  ¢   Ç  â     "  G  b    ¢  Ç  â    "  G  b    ¢  Ç    â I    " I   b I     Å  Y Å   Å  Y   ¢ I    â I    