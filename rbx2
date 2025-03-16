
global function InitControlsMenu

struct
{
	var menu
	table<var,string> buttonDescriptions
	var autoSprintSetting
	array<var> advanceControlsDisableItems
	array<var> advanceControlsVisibleItems
	array<var> advanceControlsOffVisibleItems
	var gamepadLayoutLabel
	var itemDescriptionBox
} file

void function InitControlsMenu()
{
	var menu = GetMenu( "ControlsMenu" )
	file.menu = menu

	AddMenuEventHandler( menu, eUIEvent.MENU_OPEN, OnOpenControlsMenu )
	AddMenuEventHandler( menu, eUIEvent.MENU_CLOSE, OnCloseControlsMenu )

	var button

	file.itemDescriptionBox = Hud_GetChild( menu, "LblMenuItemDescription" )

#if PC_PROG
	button = Hud_GetChild( menu, "ExtrasMenu" )
	SetupButton( button, "Extras", "Enable and control hidden features" )
	AddButtonEventHandler( button, UIE_CLICK, AdvanceMenuEventHandler( GetMenu( "ExtrasMenu" ) ) )

	button = Hud_GetChild( menu, "BtnMouseKeyboardBindings" )
	SetupButton( button, "#KEY_BINDINGS", "#MOUSE_KEYBOARD_MENU_CONTROLS_DESC" )
	AddButtonEventHandler( button, UIE_CLICK, AdvanceMenuEventHandler( GetMenu( "MouseKeyboardBindingsMenu" ) ) )

	SetupButton( Hud_GetChild( Hud_GetChild( menu, "SldMouseSensitivity" ), "BtnDropButton" ), "#MOUSE_SENSITIVITY", "#MOUSE_KEYBOARD_MENU_SENSITIVITY_DESC" )
	SetupButton( Hud_GetChild( Hud_GetChild( menu, "SldMouseSensitivityZoomed" ), "BtnDropButton" ), "#MOUSE_SENSITIVITY_ZOOM", "#MOUSE_KEYBOARD_MENU_SENSITIVITY_ZOOM_DESC" )
	SetupButton( Hud_GetChild( menu, "SwchMouseAcceleration" ), "#MOUSE_ACCELERATION", "#MOUSE_KEYBOARD_MENU_ACCELERATION_DESC" )
	SetupButton( Hud_GetChild( menu, "SwchMouseInvertY" ), "#MOUSE_INVERT", "#MOUSE_KEYBOARD_MENU_INVERT_DESC" )
#endif //PC_PROG

	button = Hud_GetChild( menu, "BtnGamepadLayout" )
	SetupButton( button, "#BUTTON_STICK_LAYOUT", "#GAMEPAD_MENU_CONTROLS_DESC" )
	AddButtonEventHandler( button, UIE_CLICK, AdvanceMenuEventHandler( GetMenu( "GamepadLayoutMenu" ) ) )

	//button = Hud_GetChild( menu, "BtnControllerResetToDefaults" )
	//SetupButton( button, "#RESET_CONTROLLER_TO_DEFAULT", "#RESET_CONTROLLER_TO_DEFAULT_DESC" )
	//AddButtonEventHandler( button, UIE_CLICK, Controller_ResetToDefaultsDialog )

	//BtnControllerOpenAdvancedMenu
	button = Hud_GetChild( menu, "BtnControllerOpenAdvancedMenu" )
	SetupButton( button, "#OPEN_ADVANCED_LOOK_CONTROLS", "#OPEN_ADVANCED_LOOK_CONTROLS_DESC" )
	AddButtonEventHandler( button, UIE_CLICK, AdvanceMenuEventHandler( GetMenu( "ControlsAdvancedLookMenu" ) ) )

	button = SetupButton( Hud_GetChild( menu, "SwchLookSensitivity" ), "#LOOK_SENSITIVITY", "#GAMEPAD_MENU_SENSITIVITY_DESC" )
	file.advanceControlsDisableItems.append( button )

	button = SetupButton( Hud_GetChild( menu, "SwchLookSensitivityADS" ), "#LOOK_SENSITIVITY_ADS", "#GAMEPAD_MENU_SENSITIVITY_ADS_DESC" )
	file.advanceControlsDisableItems.append( button )

	SetupButton( Hud_GetChild( menu, "SwchLookInvert" ), "#LOOK_INVERT", "#GAMEPAD_MENU_INVERT_DESC" )

	button = SetupButton( Hud_GetChild( menu, "SwchLookDeadzone" ), "#LOOK_DRIFT_GUARD", "#GAMEPAD_MENU_DRIFT_GUARD_DESC" )
	file.advanceControlsDisableItems.append( button )

	SetupButton( Hud_GetChild( menu, "SwchMoveDeadzone" ), "#MOVE_DRIFT_GUARD", "#GAMEPAD_MENU_MOVE_DRIFT_GUARD_DESC" )

#if DURANGO_PROG
	button = SetupButton( Hud_GetChild( menu, "SwchLookAiming" ), "#LOOKSTICK_AIMING", "#GAMEPAD_MENU_LOOK_AIMING_DESC_DURANGO" )
#else // #if DURANGO_PROG
	button = SetupButton( Hud_GetChild( menu, "SwchLookAiming" ), "#LOOKSTICK_AIMING", "#GAMEPAD_MENU_LOOK_AIMING_DESC" )
#endif // #if DURANGO_PROG
	file.advanceControlsDisableItems.append( button )

	SetupButton( Hud_GetChild( menu, "SwchVibration" ), "#VIBRATION", "#GAMEPAD_MENU_VIBRATION_DESC" )
	SetupButton( Hud_GetChild( menu, "SwchHoldToCrouch" ), "#HOLDTOCROUCH", "#GAMEPAD_MENU_HOLDTOCROUCH_DESC" )
	SetupButton( Hud_GetChild( menu, "SwchToggleGamepadADS" ), "#GAMEPAD_TOGGLE_ADS", "#GAMEPAD_TOGGLE_ADS_DESC" )

	file.autoSprintSetting = Hud_GetChild( menu, "SwchAutoSprint" )
	SetupButton( file.autoSprintSetting, "#MENU_AUTOMATIC_SPRINT", "#OPTIONS_MENU_AUTOSPRINT_DESC" )

	SetupButton( Hud_GetChild( menu, "SwchHoldToRodeo" ), "#MENU_HOLD_TO_RODEO", "#MENU_HOLD_TO_RODEO_DESC" )
	SetupButton( Hud_GetChild( menu, "SwchEnableCheats" ), "Enable Cheats", "Enables extra options not usually available such as:\n\n- `1sv_gravity`0\n\n- `1host_timescale`0\n\n- `1thirdperson`0" )

	file.advanceControlsVisibleItems.append( Hud_GetChild( menu, "SwchLookSensitivity_AdvLabel" ) )
	file.advanceControlsVisibleItems.append( Hud_GetChild( menu, "SwchLookSensitivityADS_AdvLabel" ) )
	file.advanceControlsVisibleItems.append( Hud_GetChild( menu, "SwchLookAiming_AdvLabel" ) )
	file.advanceControlsVisibleItems.append( Hud_GetChild( menu, "SwchLookDeadzone_AdvLabel" ) )
	file.advanceControlsVisibleItems.append( Hud_GetChild( menu, "LblAdvControllerOn" ) )

	file.advanceControlsOffVisibleItems.append( Hud_GetChild( menu, "LblAdvControllerOff" ) )

	file.gamepadLayoutLabel = Hud_GetChild( menu, "LblGamepadLayout" )

#if PC_PROG
	AddEventHandlerToButtonClass( menu, "RuiFooterButtonClass", UIE_GET_FOCUS, FooterButton_Focused )
#endif //PC_PROG

	AddMenuFooterOption( menu, BUTTON_A, "#A_BUTTON_SELECT" )
	AddMenuFooterOption( menu, BUTTON_B, "#B_BUTTON_BACK", "#BACK" )
	AddMenuFooterOption( menu, BUTTON_BACK, "#BACKBUTTON_RESTORE_DEFAULTS", "#RESET_CONTROLLER_TO_DEFAULT", Controller_ResetToDefaultsDialog )

#if CONSOLE_PROG
	AddMenuFooterOption( menu, BUTTON_SHOULDER_LEFT, "#LS_BUTTON_REVIEW_TERMS", "#REVIEW_TERMS", OpenReviewTermsDialog, AreTermsAccepted ) // Console only, waiting on PC text
#endif // CONSOLE_PROG
#if DURANGO_PROG
	AddMenuFooterOption( menu, BUTTON_Y, "#Y_BUTTON_XBOX_HELP", "", OpenXboxHelp )
#endif // DURANGO_PROG
}

bool function IsAffectedByAdvancedControls( var button )
{
	foreach( var item in file.advanceControlsDisableItems )
	{
		if ( item == button )
			return true
	}
	return false
}

void function SetStatesForCustomEnable()
{
	bool customGamepadIsEnabled = GetConVarBool( "gamepad_custom_enabled" )

	foreach( var item in file.advanceControlsDisableItems )
		Hud_SetEnabled( item, !customGamepadIsEnabled )

	foreach( var item in file.advanceControlsVisibleItems )
		Hud_SetVisible( item, customGamepadIsEnabled )
	foreach( var item in file.advanceControlsOffVisibleItems )
		Hud_SetVisible( item, !customGamepadIsEnabled )
}

void function RefreshGamepadLayoutLabel()
{
	Hud_SetText( file.gamepadLayoutLabel, GetGamepadButtonLayoutName() )

	int id = GetConVarInt( "gamepad_button_layout" )
	if ( id == 0 )
		Hud_SetColor( file.gamepadLayoutLabel, 255, 255, 255, 127 )
	else
		Hud_SetColor( file.gamepadLayoutLabel, 244, 213, 166, 255 )
}

void function OnOpenControlsMenu()
{
	UI_SetPresentationType( ePresentationType.NO_MODELS )

	Hud_SetEnabled( file.autoSprintSetting, !IsAutoSprintForced() )

	RefreshGamepadLayoutLabel()

	SetStatesForCustomEnable()
}

void function OnCloseControlsMenu()
{
	if ( IsConnected() )
	{
		int holdToRodeoState = GetConVarInt( "cl_hold_to_rodeo_enable" )
		ClientCommand( "HoldToRodeo " + holdToRodeoState )
	}

	SavePlayerSettings()
}

void function OnOpenExtrasMenu()
{
	UI_SetPresentationType( ePresentationType.NO_MODELS )

	Hud_SetEnabled( file.autoSprintSetting, !IsAutoSprintForced() )

	RefreshGamepadLayoutLabel()

	SetStatesForCustomEnable()
}

void function OnCloseExtrasMenu()
{
	if ( IsConnected() )
	{
		int holdToRodeoState = GetConVarInt( "cl_hold_to_rodeo_enable" )
		ClientCommand( "HoldToRodeo " + holdToRodeoState )
	}

	SavePlayerSettings()
}

var function SetupButton( var button, string buttonText, string description )
{
	SetButtonRuiText( button, buttonText )
	file.buttonDescriptions[ button ] <- description
	AddButtonEventHandler( button, UIE_GET_FOCUS, Button_Focused )
	return button
}

void function Button_Focused( var button )
{
	string description = file.buttonDescriptions[button]
	RuiSetString( Hud_GetRui( file.itemDescriptionBox ), "description", description )
}

void function Controller_ResetToDefaultsDialog( var button )
{
	DialogData dialogData
	dialogData.header = "#RESET_CONTROLLER_TO_DEFAULT_DIALOG"
	dialogData.message = "#RESET_CONTROLLER_TO_DEFAULT_DIALOG_DESC"
	AddDialogButton( dialogData, "#RESTORE", Controller_ResetToDefaults )
	AddDialogButton( dialogData, "#CANCEL" )
	OpenDialog( dialogData )

	EmitUISound( "menu_accept" )
}

void function Controller_ResetToDefaults()
{
	SetConVarToDefault( "autosprint_type" )
	SetConVarToDefault( "cl_hold_to_rodeo_enable" )
	SetConVarToDefault( "sv_cheats" )

	SetConVarToDefault( "gamepad_togglecrouch_hold" )
	SetConVarToDefault( "gamepad_toggle_ads" )
	SetConVarToDefault( "gamepad_aim_speed" )
	SetConVarToDefault( "gamepad_aim_speed_ads" )
	SetConVarToDefault( "joy_inverty" )
	SetConVarToDefault( "gamepad_look_curve" )
	SetConVarToDefault( "gamepad_deadzone_index_look" )
	SetConVarToDefault( "gamepad_deadzone_index_move" )
	SetConVarToDefault( "joy_rumble" )

	SetConVarToDefault( "gamepad_button_layout" )
	SetConVarToDefault( "gamepad_buttons_are_southpaw" )
	SetConVarToDefault( "gamepad_stick_layout" )

	SetConVarToDefault( "gamepad_custom_pilot" )
	SetConVarToDefault( "gamepad_custom_titan" )

	SetConVarToDefault( "gamepad_custom_enabled" )
	SetStatesForCustomEnable()

	ExecConfig( "gamepad_stick_layout_default.cfg" )
	ExecConfig( "gamepad_button_layout_default.cfg" )

#if PC_PROG
	SetConVarToDefault( "mouse_sensitivity" )
	SetConVarToDefault( "mouse_sensitivity_zoomed" )
	SetConVarToDefault( "m_acceleration" )
	SetConVarToDefault( "m_invert_pitch" )
#endif //PC_PROG

	RefreshGamepadLayoutLabel()
	EmitUISound( "menu_advocategift_open" )
}

#if PC_PROG
void function FooterButton_Focused( var button )
{
	RuiSetString( Hud_GetRui( file.itemDescriptionBox ), "description", "" )
}
#endif //PC_PROG
