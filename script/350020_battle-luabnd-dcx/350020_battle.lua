LuaP		¶	hçõ}A       =(none)                              RegisterTableGoal &       GOAL_DosouSkeletonSickle350020_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate         DosouSkeletonSickle350020_Act01         DosouSkeletonSickle350020_Act02         DosouSkeletonSickle350020_Act03         DosouSkeletonSickle350020_Act04         DosouSkeletonSickle350020_Act05         DosouSkeletonSickle350020_Act15         DosouSkeletonSickle350020_Act30         DosouSkeletonSickle350020_Act31         DosouSkeletonSickle350020_Act32         DosouSkeletonSickle350020_Act40         DosouSkeletonSickle350020_Act41         DosouSkeletonSickle350020_Act42 /       DosouSkeletonSickle350020_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt .       GOAL_DosouSkeletonSickle350020_AfterAttackAct            2                                      :                 9          Init_Pseudo_Global        Common_Clear_Param        GetDist        TARGET_ENE_0        GetRandam_Int       ð?      Y@       GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        HasSpecialEffectId        TARGET_SELF     È@       GetEventRequest     Ò@      $@     D@      @      D@      4@      >@      @       @       GetTeamOrder        ORDER_TYPE_Role        ROLE_TYPE_Kankyaku       @      ?@       ROLE_TYPE_Torimaki       @             Q@      .@       InsideRange      Àb@     ÀX@      @@      N@     f@       SetCoolTime      §@     ¬§@       REGIST_FUNC         DosouSkeletonSickle350020_Act01         DosouSkeletonSickle350020_Act02         DosouSkeletonSickle350020_Act03         DosouSkeletonSickle350020_Act04         DosouSkeletonSickle350020_Act05         DosouSkeletonSickle350020_Act15         DosouSkeletonSickle350020_Act30         DosouSkeletonSickle350020_Act31         DosouSkeletonSickle350020_Act32         DosouSkeletonSickle350020_Act40         DosouSkeletonSickle350020_Act41       E@        DosouSkeletonSickle350020_Act42 /       DosouSkeletonSickle350020_ActAfter_AdjustSpace        Common_Battle_Activate     ë         Y
  
  
  E      	Y ¿ Å  ¿ A 	 
 KÀ  
ËÀ 	 Á  	Á 
 
ËÀ  A   B T  	Â    	ÃÃÔ 	Â	Â	ÃÔ Õ? Ô Ä Å   T  T  	@Ô 	ÀT Õ? T Ä Å Å  Ô  T  	@T 	CÉBÉÂT   ÉÅÉÅ	FICÉEÉÂ
        A A A   ÉÂ	CÉB	CÉÂIÃT ÉÅGÉBÉÂIÃÔ      A A	 A  Ô  	ÆIÃÉÂT  É¿É¿	     Á	  ÅA É	     
 Á FÆA É  Õ   ÉÅE
     
  ÉE
     Å
  ÉE
       ÉE
     E  ÉE
       ÉE
     Å  ÉE
       ÉE
     E  ÉE
       ÉE
     Å  ÉE
       ÉE
       ÉE
     Å            Y          å                    !       AddObserveSpecialEffectAttribute        TARGET_SELF      Ñ@      @       GetMapHitRadius               I@       @       Approach_Act_Flex      §@     §@       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin       $@       TARGET_ENE_0        GOAL_COMMON_ComboFinal        GetWellSpace_Odds     8   > E    Y ? E  Í~Ì¿ÀA A Á  Á 	 
               Y 
A 
 Á  Á  A A KÁ  A      A A A A YKÁ Å A    A A YA                                 !       AddObserveSpecialEffectAttribute        TARGET_SELF      Ñ@      @       GetMapHitRadius               I@      @       @       Approach_Act_Flex      §@      @       AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       TARGET_ENE_0        GetWellSpace_Odds     0   > E    Y ? E  Í~Ì¿ÀA A Á  	E 
               Y 
 
? E  ÍA A Á E    Å     A A YA                                       4@       GetMapHitRadius        TARGET_SELF               I@      @       @       Approach_Act_Flex        GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0       ø?       AddSubGoal        GOAL_COMMON_LeaveTarget       @       @      ð¿     §@       GOAL_COMMON_AttackTunableSpin       $@       GetWellSpace_Odds     >   Ë>   Í }L¿¿Á  Á  A  	Å 
               Y 
@ 
A   
KA  ×Á  Â Å   A     YÁ Ë>   MÁ  Á  Â  A        Á  Á  YÁ               @                
        §@      @       GetMapHitRadius        TARGET_SELF                AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       TARGET_ENE_0        GetWellSpace_Odds          ? Å  }  Ë¿  	Á 
         Y G E            _                         @       GetMapHitRadius        TARGET_SELF               I@      @       @       Approach_Act_Flex      §@      @       AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       TARGET_ENE_0        GetWellSpace_Odds     ,   Ë>   Í }L¿¿Á  Á  A  	Å 
               Y 
 
Ë>   ÍÁ  Á  Á Å    E     Á  Á  YÁ               x                         *@              I@      Y@      @       @       Approach_Act_Flex !       AddObserveSpecialEffectAttribute        TARGET_SELF     0Ñ@     ¬§@      @       GetRandam_Int       ð?       AddSubGoal #       GOAL_COMMON_ComboAttackTunableSpin       $@       TARGET_ENE_0        GetWellSpace_Odds     /     Ì¾¿Á  A   A 	 
               Y 
K@ 
 A Y 
 
Á Á A  A  A A Á   Â Å    E     A  A  YA                                  !       AddObserveSpecialEffectAttribute        TARGET_SELF      Ñ@       AddSubGoal        GOAL_COMMON_SidewayMove        GetRandam_Float        @      @       TARGET_ENE_0        GetRandam_Int               ð?      >@     F@      ð¿       GetWellSpace_Odds        > E    Y K¿  Ë?  Á 	  Ë@  
Á  Ë@ 	 A  	 
  Y  Ç Å            ¨                          GetDist        TARGET_ENE_0        GetRandam_Float        @      @      @      ð?      ð¿       AddSubGoal        GOAL_COMMON_ApproachTarget        TARGET_SELF        GetWellSpace_Odds                > E  ? Á    ?  A  Á À E 	  
E       Y Ç Å            Ã                          GetDist        TARGET_ENE_0        GetRandam_Float        @      @      @      ð?      ð¿      @       AddSubGoal        GOAL_COMMON_LeaveTarget        @       GetWellSpace_Odds             &   > E  ? Á    ?  A  Á Ö  T ËÀ  	 
E  Á E    Á Y ËÀ  	 
E   E    Á YA              Û                          GetRandam_Int       ð?      Y@       GetDist        TARGET_ENE_0 !       AddObserveSpecialEffectAttribute        TARGET_SELF      Ñ@      >@     §@      @       GetMapHitRadius                AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       GetWellSpace_Odds     $   > A     K?  Ë?  Á Y @ T A KA    ËÁ 	 Á          Y	              ó                
        Ó@      @       GetMapHitRadius        TARGET_SELF                AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       TARGET_ENE_0        GetWellSpace_Odds          ? Å  }  Ë¿  	Á 
         Y G E                               !       AddObserveSpecialEffectAttribute        TARGET_SELF      Ñ@       GetDist        TARGET_ENE_0        GetRandam_Float        @      @      @      ð?      ð¿      @       AddSubGoal        GOAL_COMMON_LeaveTarget        @       GetWellSpace_Odds             *   > E    Y K?  Ë?  Á  Ë? Á    Ö T Á E 	Á 
      Y Á E 	Á 
 Á     Y Ç Å                                      AddSubGoal .       GOAL_DosouSkeletonSickle350020_AfterAttackAct       $@       ¾ E    Y           #                          Update_Default_NoSubGoal                              +                                     4                   !       AddObserveSpecialEffectAttribute        TARGET_SELF      Ñ@       HasSpecialEffectId        ClearSubGoal         DosouSkeletonSickle350020_Act41        ¾ E    Y K¿ E     Ô ?Y E     Y               L                                     R                          Update_Default_NoSubGoal                      @      E  A  Y    E   Y Å   "  I  Å   b  I ¢     â   Ç  "    b  G  ¢    â  Ç  "    b  G  ¢    â  Ç  "    b  G  ¢    Å   â I Å   " I  Å   b I      Y      Y Å   ¢ I Å   â I   